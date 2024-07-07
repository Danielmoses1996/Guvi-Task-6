from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Define endpoint for model prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0][1]
    return jsonify({'prediction': int(prediction), 'probability': float(probability)})

if __name__ == '__main__':
    app.run(debug=True)
