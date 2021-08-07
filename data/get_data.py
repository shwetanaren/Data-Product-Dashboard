import streamlit as st 
import pandas as pd

# DATE_TIME = "date/time"

@st.cache

def load_dataset(url):
    data = pd.read_csv(url)
    # data.rename(lowercase, axis="columns", inplace=True)
    # data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data



