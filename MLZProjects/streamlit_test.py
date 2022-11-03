import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import time, datetime



st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3, clo4 = st.columns(4)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')
  st.header('st.selectbox')

  option1 = st.selectbox(
         'What is your favorite color?',
              ('Yes', 'No'))

#st.write('Your favorite color is ', option1)

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')
    
  st.header('st.selectbox')
  option2 = st.selectbox(
         'Sex?',
              ('Male', 'Female'))   
  #st.write('Your favorite color is ', option2) 

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
  option3 = st.selectbox(
         'Age?',
              ('1', '2','3'))   
  #st.write('Your favorite color is ', option2) 






st.title('Diabetes Prediction from Health Indicators')
st.text('Behavioral Risk Factor Surveillance System BRFFS - CDC')

###############
st.header('st.selectbox')
#
#option = st.selectbox(
#     'What is your favorite color?',
#     ('Blue', 'Red', 'Green'))
#
#st.write('Your favorite color is ', option)

###############

def func1(): st.write("Function 1 executed.")
#def func2(): st.write("Function 2 executed.")
#def func3(): st.write("Function 3 executed.")

# function to run chosen function(s)
def execute():
    if cb1: func1()
    #if cb2: func2()
    #if cb3: func3()

# checkbox shenanigans 
cbYes = st.sidebar.checkbox("Yes")

if cbYes:
    cb1 = st.sidebar.checkbox("No",value=cbYes,disabled=True,key=1)
    #cb2 = st.sidebar.checkbox("Func 2",value=cbAll,disabled=True,key=2)
    #cb3 = st.sidebar.checkbox("Func 3",value=cbAll,disabled=True,key=3)
else:
    cb1 = st.sidebar.checkbox("No",key=4)
    #cb2 = st.sidebar.checkbox("Func 2",key=5)
    #cb3 = st.sidebar.checkbox("Func 3",key=6)

run_btn = st.sidebar.button('Run', on_click=execute, key='e')


st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)




