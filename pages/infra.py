import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from data.get_data import load_dataset

def app():
    st.title('Data driven events')
    st.write(
        """
        Examining the rate of change of events across the targeted user demographic.
        """)    


    url = '../data/Flyber_event_logs.csv'
    df = load_dataset(url)


    # LAYING OUT THE TOP SECTION OF THE APP
    row1_1, row1_2 = st.beta_columns((2,2))
    row2_1, row2_2 = st.beta_columns((2,2))

    with row1_1:
        # st.markdown("### Mapping User Preferences ")
        event_selected = st.selectbox('Select Event Type', ['mobile','web'])

    with row1_2:
        # st.markdown("### Mapping User Preferences ")
        event_selected = st.selectbox('Select XXXXX', ['mobile','web'])    


    with row2_1:
        # st.markdown("### Select  ")
        borough_selected = st.selectbox('Select the Borough', ['Manhattan','Bronx'])

    with row2_2:
        # st.markdown("### Select the age group ")
        age_selected = st.selectbox('Select Age Group', ['20s','30s','40s','50s','60s'])    


    # FILTERING DATA BY HOUR SELECTED
    df = df[df['category'] == event_selected]
    