
from dataclasses import dataclass
from flask import Flask, jsonify, render_template, request
from models.utils import MedicalInsurance
import numpy as np
import pandas as pd


app = Flask(__name__)   # create an instance of flask


@app.route('/')                # decorator of API   #  when blank / only than heating home API
def hello_flask():
    print("welcome to medical charges predition")
    # return "Success"
    return render_template("index.html")

@app.route('/predict_charges',methods=['POST','GET'])
def get_insurance_charges():
    data=request.form
    print(data)

    age = eval(data['age'])
    sex = data['sex']
    bmi = eval(data['bmi'])
    children = eval(data['children'])
    smoker = data['smoker']
    region = data['region']

    med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
    charges = med_ins.get_predicted_price()
    print()
    return jsonify({"Result",f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only"})



if __name__=="__main__":
    app.run()

    # app.run(host='0.0.0.0',PORT_NUMBER=config.5000,debug=True)