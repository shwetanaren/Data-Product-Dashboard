import streamlit as st
import numpy as np
import pandas as pd
from data.get_data import load_dataset

def app():
    st.title('Reporting Metrics on the Success metrics and MVP launch')

    
    url = '../data/'
    df = load_dataset(url)


    # LAYING OUT THE TOP SECTION OF THE APP
    row1_1, row1_2 = st.beta_columns((2,3))
    row2_1, row2_2 = st.beta_columns((2,2))

    with row1_1:
        st.markdown("### Mapping User Preferences ")
        gender_selected = st.selectbox('Select Gender', ['M','F'])

    with row1_2:
        st.write(
        """
        ##
        Examining the price comparison of Flying taxi by user demographics.
        """)    

    with row2_1:
        st.markdown("### Select the Income level ")
        income_selected = st.selectbox('Select', ['100,000+','20,000-50,000'])

    with row2_2:
        st.markdown("### Select the age group ")
        age_selected = st.selectbox('Select Age', ['20s','30s','40s','50s','60s'])    


    # FILTERING DATA BY HOUR SELECTED
    df = df[df['q2_gender'] == gender_selected]
    