import streamlit as st
import eda
import prediction

# page
page = st.sidebar.selectbox('Pilih Halaman',('EDA','Prediction'))

if page == 'EDA':
    eda.run()
else:
    prediction.run()