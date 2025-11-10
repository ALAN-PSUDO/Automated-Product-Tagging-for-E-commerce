import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Input, Dense, GlobalAveragePooling2D, Dropout, BatchNormalization
from tensorflow.keras.models import Model
import os

gdrive_file_id = "17Snw7qDy_Pw1_1k5TvcFhpDEZDEehPJl"

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
    
    color_out = Dense(10, activation='sigmoid', name='color')(x)
    product_out = Dense(10, activation='sigmoid', name='product')(x)
    
    model = Model(inputs=inp, outputs=[color_out, product_out])
    return model

if os.path.exists('best_model.h5'):
    print("Model file found! Loading existing model...")
    print("(delete best_model.h5 if you want to rebuild)")
    model = tf.keras.models.load_model('best_model.h5')
else:
    print("Model not found...")
    
    try:
        import gdown
        url = f'https://drive.google.com/uc?id={gdrive_file_id}'
        print("Downloading from Google Drive...")
        gdown.download(url, 'best_model.h5', quiet=False)
        print("Download done!")
        model = tf.keras.models.load_model('best_model.h5')
    except:
        print("Download failed or gdown not installed")
        print("Building model from scratch...")
        
        model = build_model()
        
        model.compile(
            optimizer='adam',
            loss='binary_crossentropy',
            metrics=['accuracy']
        )
        
        print("\nModel architecture:")
        model.summary()
        
        print("\nSaving model...")
        model.save('best_model.h5')
        print("Model saved as best_model.h5")

total = model.count_params()
print(f"\nTotal parameters: {total:,}")
