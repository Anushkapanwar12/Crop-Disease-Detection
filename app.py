from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import numpy as np
from model import predict   # import your model function

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})

    file = request.files['image']
    image = Image.open(file.stream)

    result = predict(image)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)