
import streamlit as st
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from datetime import time, datetime
from Predict import predict
from utils import InputData, Description

st.set_page_config(layout="wide")


st.markdown("<h1 style='text-align: center; color: black; font-size: 45px'>Diabetes Probability Calculator</h1>", unsafe_allow_html=True)
st.write("#")
st.write("#")

# Descripion of the project
desc = Description()

html_str = f"""
            <style>
            p.a {{font-size: 18px;}}
            </style>
            <p class="a">
            {desc}
            </p>
            """

st.markdown(html_str, unsafe_allow_html=True)

# Getting data inputs

st.write("#")
st.write("#")

st.subheader('Select a patient or try it yourself')
patient = st.selectbox('Patient', ['Patient # 1', 'Patient # 2', 'Myself'], key='Patient # 1')
st.write("#")

patients = InputData()

defaultInput = patients[patient]

with st.form(key='columns_in_form'):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.subheader('Demographics')
        sex = st.selectbox('sex', ['Male', 'Female'], key=defaultInput['sex'])
        age = st.slider('How old are you?', 18, 99, value=defaultInput['age'])
        education = st.selectbox('What is your level of education?',
                                ['Never attended school or only kindergarten',
                                'Elementary school',
                                'Some high school',
                                'High school graduate',
                                'Some college or technical school',
                                'College graduate'],
                                index=5)
        income = st.selectbox('What is your income?',
                            ['less than $10,000','$10,000 to $15,000','$15,000 to $20,000','$20,000 to $25,000',
                            '$25,000 to $35,000','$35,000 to $50,000','$50,000 to $75,000','$75,000 or  more'],
                            index=7)
        bmi = st.slider("What's your BMI?", 10, 99, value=defaultInput['bmi'])

    with c2:
        st.subheader('Overall Health')
        genhealth = st.selectbox('Your general health is', ['Excellent', 'Very good', 'Good', 'Fair', 'Poor'], index=2)
        menthlth  = st.slider('How many days during the past 30 days was your mental health not good?', 0, 30, value=defaultInput['menthlth'])
        physhlth = st.slider('How many days during the past 30 days was your physical health not good?', 0, 30, value=defaultInput['physhlth'])
        diffwalk = st.selectbox('Do you have serious difficulty walking or climbing stairs?', ['Yes', 'No'], index=1)

    with c3:
        st.subheader('Medical Conditions')
        highcolesterol = st.selectbox('A doctor, nurse, or health professional have told you have high blood cholesterol', ['Yes', 'No'], index=1)
        colesterolcheck = st.selectbox('Have you had a cholesterol check in the past 5 years?', ['Yes', 'No'], index=0)
        stroke = st.selectbox('Have you ever been told you had a stroke', ['Yes', 'No'], index=1)
        coronary = st.selectbox('Do you have any coronary heart disease or have had a myocardial infarction', ['Yes', 'No'], index=1)

    with c4:
        st.subheader('Other questions')
        bloodpress = st.selectbox('A doctor, nurse, or health professional have told you have high blood pressure', ['Yes', 'No'], index=1)
        smoker = st.selectbox('Have you smoked at least 100 cigarettes in your entire life', ['Yes', 'No'], index=0)
        excercise = st.selectbox('Any physical activity or exercise during the past 30 days (not including work)?', ['Yes', 'No'], index=0)
        alcohol = st.selectbox('Are you a heavy drinkers? Adult men: 14+   -   Adult woman: 7+   (drinks/week)', ['Yes', 'No'], index=1)
        #coffee_roast_val4 = st.selectbox('Coffee roast4', ['Light', 'Medium', 'Dark'])
        #milk_val4 = st.select_slider('Milk intensity4', ['None', 'Low', 'Medium', 'High'])
        #owncup_val4 = st.checkbox('Bring own cup4')


    submitButton = st.form_submit_button(label = 'Calculate')

inputData = {
    "highbp"                : bloodpress,
    "highchol"              : highcolesterol,
    "cholcheck"             : colesterolcheck, 
    "bmi"                   : bmi,
    "smoker"                : smoker,
    "stroke"                : stroke,
    "heartdiseaseorattack"  : coronary,
    "physactivity"          : excercise,
    "hvyalcoholconsump"     : alcohol,
    "genhlth"               : genhealth,
    "menthlth"              : menthlth,
    "physhlth"              : physhlth,
    "diffwalk"              : diffwalk,
    "sex"                   : sex,
    "age"                   : age,
    "education"             : education,
    "income"                : income,
}

st.write("#")
st.write("#")

##################
c1, c2, c3, c4, c5 = st.columns(5)



results, deltas = predict(inputData)

with c1:


    st.subheader('DecisionTreeClassifier')
    st.metric(label = "Probability of diabetes", value = str(results['DecisionTreeClassifier']) + ' %', delta=deltas['DecisionTreeClassifier'])

with c2:

    st.subheader('LogisticRegression')
    st.metric(label = "Probability of diabetes", value = str(results['LogisticRegression']) + ' %', delta=deltas['LogisticRegression'])

with c3:



    st.subheader('RandomForestClassifier')
    st.metric(label = "Probability of diabetes", value = str(results['RandomForestClassifier']) + ' %', delta=deltas['RandomForestClassifier'])

with c4:

    st.subheader('XGBClassifier')
    st.metric(label = "Probability of diabetes", value = str(results['XGBClassifier']) + ' %', delta=deltas['XGBClassifier'])

with c5:

    st.subheader('AdaBoostClassifier')
    st.metric(label = "Probability of diabetes", value = str(results['AdaBoostClassifier']) + ' %', delta=deltas['AdaBoostClassifier'])




