from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Parkinson’s Disease Detection App (Demo)"

@app.route('/predict')
def predict():
    return "Prediction: Parkinson’s Detected (Demo Output)"

if __name__ == '__main__':
    app.run(debug=True)
