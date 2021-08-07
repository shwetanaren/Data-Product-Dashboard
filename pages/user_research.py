import streamlit as st
import numpy as np
import pandas as pd
from data.get_data import load_dataset

def app():
    st.title('User Interviews Summary')

    url = '../data/4_user_research_processed.csv'
    df = load_dataset(url)


    # LAYING OUT THE TOP SECTION OF THE APP
    row1_1, row1_2 = st.beta_columns((2,3))
    row2_1, row2_2 = st.beta_columns((3,3))
    row3_1, row3_2 = st.beta_columns((3,3))

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


    with row3_1:
        st.markdown("### Select the Income level ")
        income_selected = st.selectbox('Select', ['100,000+','20,000-50,000'])

    with row3_2:
        st.markdown("### Select the age group ")
        age_selected = st.selectbox('Select Age', ['20s','30s','40s','50s','60s'])    


    # FILTERING DATA BY HOUR SELECTED
    df = df[df['q2_gender'] == gender_selected]
    