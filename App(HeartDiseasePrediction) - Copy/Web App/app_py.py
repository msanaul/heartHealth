from flask import Flask, request, render_template
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')


app = Flask(__name__)

lgr = pickle.load(open("D:\My Project Work\App(HeartDiseasePrediction)\Web App\heart-disease.pkl","rb"))

@app.route("/", methods = ['GET'])
def home():
  return render_template("index.html")

@app.route("/predict", methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        init_features = [int(x) for x in request.form.values()]
        final_features = [np.array(init_features)]
        prediction = lgr.predict(final_features)
        if prediction == 1:
              return render_template('index.html',prediction_text = "You are Fine.")
        else:
              return render_template('index.html',prediction_text = "You need treatment.")

app.run(debug=True)