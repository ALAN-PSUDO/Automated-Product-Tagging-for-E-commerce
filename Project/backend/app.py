# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import joblib
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import io
from dotenv import load_dotenv
import os
import traceback
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for Codespaces

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 5000))
DEBUG = os.getenv("FLASK_DEBUG", "False").lower() == "true"

# ===========================
# Load models and data
# ===========================
BASE_DIR = os.path.dirname(__file__)
MODEL_DIR = os.path.join(BASE_DIR, "models")

cnn_model_path = os.path.join(MODEL_DIR, "best_model.h5")
cnn_model = load_model(cnn_model_path)
print("✅ Loaded CNN model:", cnn_model_path)

xgb_model_path = os.path.join(MODEL_DIR, "xgb_price_model.pkl")
xgb_model = joblib.load(xgb_model_path)
print("✅ Loaded XGBoost model:", xgb_model_path)

csv_path = os.path.join(MODEL_DIR, "merged_articles_transactions.csv")
df_ref = pd.read_csv(csv_path)
categorical_columns = [
    "product_type_name", "product_group_name", "graphical_appearance_name",
    "colour_group_name", "perceived_colour_value_name", "perceived_colour_master_name",
    "department_name", "index_group_name", "section_name", "garment_group_name"
]
for col in categorical_columns:
    if col not in df_ref.columns:
        df_ref[col] = ""
df_ref = pd.get_dummies(df_ref, columns=categorical_columns, drop_first=True)
feature_columns = [col for col in df_ref.columns if col != "price"]
print(f"✅ Data reference loaded with {len(feature_columns)} features.")

# ===========================
# Preprocessing helpers
# ===========================
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((224, 224))
    img_arr = np.array(img) / 255.0
    img_arr = np.expand_dims(img_arr, axis=0)
    return img_arr

def preprocess_tabular(data_json):
    row = pd.DataFrame([data_json])
    for col in categorical_columns:
        if col not in row:
            row[col] = ""
    row_encoded = pd.get_dummies(row, columns=categorical_columns, drop_first=True)
    for col in feature_columns:
        if col not in row_encoded.columns:
            row_encoded[col] = 0
    row_encoded = row_encoded[feature_columns]
    return row_encoded

# ===========================
# Prediction endpoint
# ===========================
@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        image = request.files["file"]
        img_bytes = image.read()
        img_input = preprocess_image(img_bytes)

        cnn_pred = cnn_model.predict(img_input)
        if hasattr(cnn_pred, "tolist"):
            cnn_pred = cnn_pred.tolist()
        elif isinstance(cnn_pred, (list, tuple)):
            cnn_pred = list(cnn_pred)
        else:
            cnn_pred = [float(cnn_pred)]

        print("✅ CNN prediction shape:", np.array(cnn_pred).shape)

        metadata_str = request.form.get("metadata")
        if metadata_str:
            try:
                metadata = json.loads(metadata_str)
            except:
                metadata = eval(metadata_str)

            df_input = preprocess_tabular(metadata)

            # Drop unwanted columns like article_id to match training data
            if "article_id" in df_input.columns:
                df_input = df_input.drop(columns=["article_id"])

            xgb_pred = float(xgb_model.predict(df_input)[0])
        else:
            xgb_pred = None

        # ✅ Convert NumPy outputs to JSON-safe Python types
        cnn_pred = np.array(cnn_pred).tolist()
        xgb_pred = float(xgb_pred) if xgb_pred is not None else None

        return jsonify({
            "cnn_output": cnn_pred,
            "predicted_price": xgb_pred
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# ===========================
# Health endpoint
# ===========================
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask backend is running successfully!"})

# ===========================
# Main entry
# ===========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
