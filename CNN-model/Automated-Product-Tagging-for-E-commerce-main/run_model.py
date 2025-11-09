import tensorflow as tf
import numpy as np

# Load the model
model = tf.keras.models.load_model("best_model.h5")

# Print a summary
model.summary()

# Example: run inference on dummy data
# (replace this with your real input)
input_data = np.random.rand(1, *model.input_shape[1:])  # shape matches model input
predictions = model.predict(input_data)

print("Predictions:", predictions)
