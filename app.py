import streamlit as st
from multiapp import MultiApp
from pages import home, data_stats, user_research, geo_data, reporting_metrics, infra # import your application pages here

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

app = MultiApp()

st.sidebar.header('Thin Slice of a Data Product')
# Import all your application views here

app.add_app("About", home.app)
app.add_app("I - Temporal Analysis", data_stats.app)
app.add_app("I - Geographic Data Analysis", geo_data.app)
app.add_app("I - User Research", user_research.app)
# app.add_app("II - A/B Test results", geo_data.app)
# app.add_app("III - Data Infrastructure", infra.app)
# app.add_app("IV - Iterative Product Development", reporting_metrics.app)

# The main app
app.run()

