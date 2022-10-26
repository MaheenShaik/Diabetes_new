# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 21:38:41 2022

@author: Maheen
"""

import pickle
import streamlit as st

#loading the saved models
diabetes_model=pickle.load(open('diabetes_model.sav','rb'))

st.title('Diabetes Prediction using ML')
    
    #getting the input data from user
    #columns for input fields
    
col1,col2,col3=st.columns(3)

with col1:
    Pregnancies=st.text_input('Number of Pregnancies')
with col2:
    Glucose=st.text_input('Glucose level')
with col3:
    BloodPressure=st.text_input('BloodPressure Value')
with col1:
    SkinThickness=st.text_input('SkinThickness Value')
with col2:
    Insulin=st.text_input('Insulin level')
with col3:
    BMI=st.text_input('BMI Value')
with col1:
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
with col2:
    Age=st.text_input('Age of the Person') 
    
diab_diagnosis=''

#creating a button for prediction
if st.button('Diabetes Test Result'):
    diab_pred=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
    if(diab_pred[0]==1):
        diab_diagnosis='The person is diabetic'
        
    else:
        diab_diagnosis='The person is not diabetic'
st.success(diab_diagnosis)
        
    
    
        