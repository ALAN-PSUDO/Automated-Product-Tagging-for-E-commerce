import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Input, Dense, GlobalAveragePooling2D, Dropout, BatchNormalization
from tensorflow.keras.models import Model
import os

GOOGLE_DRIVE_FILE_ID = "YOUR_FILE_ID_HERE"
MODEL_PATH = 'best_model.h5'

def build_model():
    inp = Input(shape=(224, 224, 3))
    base = ResNet50(weights='imagenet', include_top=False, input_tensor=inp)
    for layer in base.layers:
        layer.trainable = False
    x = base.output
    x = GlobalAveragePooling2D()(x)
    x = BatchNormalization()(x)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.5)(x)
    x = BatchNormalization()(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.3)(x)
    color = Dense(10, activation='sigmoid', name='color')(x)
    product = Dense(10, activation='sigmoid', name='product')(x)
    model = Model(inputs=inp, outputs=[color, product])
    return model

def download_from_gdrive(file_id, destination):
    try:
        import gdown
        url = f'https://drive.google.com/uc?id={file_id}'
        print(f"Downloading model from Google Drive...")
        gdown.download(url, destination, quiet=False)
        print("Download complete!")
    except ImportError:
        print("ERROR: 'gdown' library not installed.")
        print("Install it with: pip install gdown")
        print(f"\nOr download manually from:")
        print(f"https://drive.google.com/file/d/{file_id}/view")
        exit(1)

if os.path.exists(MODEL_PATH):
    print(f"Model already exists at '{MODEL_PATH}'. Skipping build.")
    print("To rebuild, delete the existing model file first.")
else:
    if GOOGLE_DRIVE_FILE_ID != "YOUR_FILE_ID_HERE":
        print(f"Model not found. Attempting to download from Google Drive...")
        download_from_gdrive(GOOGLE_DRIVE_FILE_ID, MODEL_PATH)
    else:
        print("Building new model...")
        model = build_model()
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        model.summary()
        model.save(MODEL_PATH)
        print(f"Model saved to '{MODEL_PATH}'")
    
