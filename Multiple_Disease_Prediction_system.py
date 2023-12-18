# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 18:44:01 2023

@author: DELL
"""

import pandas as pd 
import numpy as np 
import pickle
from streamlit_option_menu import option_menu
import streamlit as st

Diabate_model = pickle.load(open("C:/Users/DELL/Downloads/Diabate_data-set/Multiple_Disease_Prediction/Dibetic_model.sav", 'rb'))

heart_disease_model= pickle.load(open("C:/Users/DELL/Downloads/Diabate_data-set/Multiple_Disease_Prediction/heart_Disease.sav", 'rb'))


#sidebar

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', ['Diabates Prediction','Heart Prediction'],
    default_index=0)
    
    
#diabatecs prediction page 
if(selected=='Diabates Prediction'):
    #page title 
    
    st.title('Diabetes Prediction')
    
    Pregnancies=st.text_input('Number of  Pregnancies')
    Glucose=st.text_input('Glucose')
    BloodPressure=st.text_input('BloodPressure')
    SkinThickness=st.text_input('SkinThickness')
    Insulin=st.text_input('Insulin')
    BMI=st.text_input('BMI')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
    Age=st.text_input('Age')
    
    #code for prediction diabates
    dia_diagonis=''
    
    
    #create a button
    if st.button('Diabates Test-Result'):
        dia_diagonis=Diabate_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(dia_diagonis[0]==1):
            dia_diagonis='The Person is Diabetics'
        else:
            dia_diagonis='The person Is not Diabetics'
            st.success(dia_diagonis)  


    
        
    
    
if selected == 'Heart Prediction':
    st.title('Heart Prediction')

    # Input fields
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain types')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholestoral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by flourosopy')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    # Code for Prediction
    heart_diagnosis = ''

    # Button for Prediction
    if st.button('Heart Disease Test Result'):
        # Check if any input field is empty
        if any(value == '' for value in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
            st.warning('Please fill in all fields before making a prediction.')
        else:
            # Convert values to float
            age = float(age)
            sex = float(sex)
            cp = float(cp)
            trestbps = float(trestbps)
            chol = float(chol)
            fbs = float(fbs)
            restecg = float(restecg)
            thalach = float(thalach)
            exang = float(exang)
            oldpeak = float(oldpeak)
            slope = float(slope)
            ca = float(ca)
            thal = float(thal)

            # Make the prediction
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

            # Display the result
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is predicted to have heart disease.'
            else:
                heart_diagnosis = 'The person is predicted not to have heart disease.'

    st.success(heart_diagnosis)

    
    
    
    


        
    