from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = []
    for feature in features:  
        features.append(float(request.form[feature]))
    
    data = {'features': features}
    response = requests.post('http://localhost:5000/predict', json=data)
    prediction = response.json()
    
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
