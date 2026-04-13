import numpy as np

# 🔴 LOAD YOUR MODEL HERE (only once)
# Example:
# from tensorflow.keras.models import load_model
# model = load_model("your_model.h5")

def predict(image):
    # 🔴 PREPROCESS IMAGE
    image = image.resize((224, 224))
    img = np.array(image) / 255.0
    img = np.expand_dims(img, axis=0)

    # 🔴 MODEL PREDICTION
    # prediction = model.predict(img)
    # result = np.argmax(prediction)

    # TEMP (for testing)
    result = "Healthy Leaf 🌱"

    return str(result)