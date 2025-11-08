import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Input, Dense, GlobalAveragePooling2D, Dropout, BatchNormalization
from tensorflow.keras.models import Model

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

print("Building model...")
model = build_model()
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()
model.save('best_model.h5')
print("Model saved")
    
