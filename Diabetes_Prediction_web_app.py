# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:22:24 2022

@author: pr&d02
"""

import numpy as np
import pickle
import streamlit as st

#loading the model

loaded_model = pickle.load(open('C:/Users/pr&d02/Desktop/diabetes/trained_model.sav','rb'))

#creating a function for prediction

def diabetes_prediction(input_data):
    input_data = (5,166,72,19,175,25.8,0.587,51)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'

def main():
    #title
    st.title('Diabetes Prediction Web App')
    # getting inputdata from the user
    
    Pregnancies = st.text_input('Number of Pregnancies:')
    Glucose = st.text_input('Glucose Level:')
    BloodPressure = st.text_input('BP Level:')
    SkinThickness = st.text_input('skin thickness:')
    Insulin = st.text_input('Insulin:')
    BMI = st.text_input('BMI:')
    DiabetesPredigreeFunction = st.text_input('Blood Pressure Level:')
    Age = st.text_input('Age of the person:')
    
    # code for prediction
    diagnosis = ''
    
    if st.button('Diabetes Test Result:'):
        diagnosis=diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,DiabetesPredigreeFunction, Age ])
    st.success(diagnosis)
    
if __name__ =='__main__':
    main()
