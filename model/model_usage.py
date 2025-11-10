import tensorflow as tf
import numpy as np
from PIL import Image
from .class_labels import COLORS, PRODUCTS

def predict_fashion_item(image_path):
    model = tf.keras.models.load_model('best_model.h5')
    
    img = Image.open(image_path).resize((224, 224))
    img_array = np.array(img) / 255.0
    img_batch = np.expand_dims(img_array, 0)
    
    color_probs, product_probs = model.predict(img_batch)
    
    color_idx = int(np.argmax(color_probs[0]))
    product_idx = int(np.argmax(product_probs[0]))
    
    return {
        'color': COLORS[color_idx],
        'color_confidence': float(color_probs[0][color_idx]) * 100,
        'product': PRODUCTS[product_idx],
        'product_confidence': float(product_probs[0][product_idx]) * 100
    }
