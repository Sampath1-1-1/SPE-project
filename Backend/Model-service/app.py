# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pickle
# import numpy as np
# from feature_extraction import FeatureExtraction, predict_url

# app = Flask(__name__)
# CORS(app)
# # Load the pre-trained model
# try:
#     with open('/app/model.pkl', 'rb') as file:
#         gbc = pickle.load(file)
# except FileNotFoundError:
#     raise Exception("model.pkl file not found. Ensure it is in the project directory.")

# @app.route('/api/predict', methods=['POST'])
# def predict():
#     try:
#         # Get JSON data from the request
#         data = request.get_json()
#         if not data or 'url' not in data:
#             return jsonify({
#                 'error': 'Invalid input. Please provide a URL in the JSON body.'
#             }), 400

#         url = data['url']
#         if not url:
#             return jsonify({
#                 'error': 'URL cannot be empty.'
#             }), 400

#         # Use the predict_url function from feature_extraction.py
#         result, pred = predict_url(url)

#         # Return the prediction as JSON
#         return jsonify({
#             'url': url,
#             'result': result,
#             'prediction': pred
#         }), 200

#     except Exception as e:
#         return jsonify({
#             'error': f'An error occurred: {str(e)}'
#         }), 500

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
from feature_extraction import FeatureExtraction, predict_url

app = Flask(__name__)
CORS(app)

# Determine model path based on environment
MODEL_PATH = '/app/model.pkl' if os.path.exists('/app/model.pkl') else './model.pkl'

# Load the pre-trained model
try:
    with open(MODEL_PATH, 'rb') as file:
        gbc = pickle.load(file)
except FileNotFoundError:
    raise Exception(f"model.pkl file not found at {MODEL_PATH}. Ensure it is in the project directory.")

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({
                'error': 'Invalid input. Please provide a URL in the JSON body.'
            }), 400

        url = data['url']
        if not url:
            return jsonify({
                'error': 'URL cannot be empty.'
            }), 400

        # Use the predict_url function from feature_extraction.py
        result, pred = predict_url(url)

        # Return the prediction as JSON
        return jsonify({
            'url': url,
            'result': result,
            'prediction': pred
        }), 200

    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)