import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import time, datetime

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)

user_name = 'Mario'

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')
  st.header('st.selectbox')

  option1 = st.selectbox(
         'What is your favorite color?',
              ('Yes', 'No'))
