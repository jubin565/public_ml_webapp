# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 21:42:06 2025

@author: Hotspot
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
diabatics_model=pickle.load(open('diabaticsmodel.sav','rb'))
breast_cancer_model=pickle.load(open('breastcancer.sav','rb'))


with st.sidebar:
    
    selected=option_menu('MULTIPLE DEISEASE PREDICTION SYSTEM',
                         ['Diabatics prediction', 'Breast cancer prediction'],
                         
                         icons=['activity','file-medical-fill'],
                         
                         default_index=0)
    #Diabetics prediction page
if selected == 'Diabatics prediction':
    st.title("Diabetes prediction content goes here.")
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure")
    with col1:
        SkinThickness = st.text_input("Skin Thickness")
    with col2:    
        Insulin = st.text_input("Insulin Level")
    with col3:    
        BMI = st.text_input("BMI")
    with col1:    
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
        
    Age = st.text_input("Age")
    result=''
    if st.button("Diabatics test result"):
        dia_prediction=diabatics_model.predict([[ Pregnancies,Glucose,BloodPressure,SkinThickness, Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
        if dia_prediction[0]==1:
            result="The person is diabetic"
        else:
            result="The person is not diabetic"
    st.success(result)        
            
elif selected == 'Breast cancer prediction':
    st.title("Breast cancer prediction content goes here.")
