from flask import Flask, request, render_template, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

app = Flask(__name__)
model = load_model('mnist_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    img = np.array(data['image']).reshape(1, 784)
    prediction = model.predict(img).argmax(axis=1)[0]
    return jsonify({'prediction': int(prediction)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
