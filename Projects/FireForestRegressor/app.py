import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

ridge = pickle.load(open('./models/ridge.pkl', 'rb'))
scaler = pickle.load(open('./models/scaler.pkl', 'rb'))


@app.route('/',  methods = ['GET', 'POST'])
@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Temprature = float(request.form['Temprature'])
        RH = float(request.form['RH'])
        Ws = float(request.form['Ws'])
        Rain = float(request.form['Rain'])
        FFMC = float(request.form['FFMC'])
        DMC = float(request.form['DMC'])
        Classes = float(request.form['Classes'])
        ISI = float(request.form['ISI'])
        Region = float(request.form['Region'])
        
        transformed_input = scaler.transform([[Temprature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        prediction = ridge.predict(transformed_input)
        return render_template('index.html', prediction=prediction[0]*(31/100))
    else:
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True, host='')