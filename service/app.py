from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)


pickle_in  = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def home():
    return "Hello world!"


@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    """Please insert housing variables 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: OverallQual
        in: query
        type: number
        required: true
      - name: FullBath
        in: query
        type: number
        required: true
      - name: GarageArea
        in: query
        type: number
        required: true
      - name: LotArea
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    OverallQual=float(request.args.get("OverallQual"))
    FullBath=float(request.args.get("FullBath"))
    GarageArea=float(request.args.get("GarageArea"))
    LotArea=float(request.args.get("LotArea"))


    prediction=classifier.predict([[OverallQual, FullBath, GarageArea, LotArea]])
    print(prediction)
    return "Hello the price is: $"+ str(prediction)



@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Please insert file for housing prediction
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))

    
if __name__ == '__main__':
    app.run(debug = True)
