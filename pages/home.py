import streamlit as st
import pandas as pd
import numpy as np
# from data.create_data import create_table

def app():
    
    st.title('Data Product Management')
    st.write("This is an explainer series consisting of 4 parts to inform the data centric approach to product building. All the data Visualizations are executed using Altair library. This dashboard is built using the Streamlit framework.")
    st.write("Goal: Is to build an MVP for Flying Taxi Service to test the Viability / Feasibility / Desirability of the product. The dataset used here is rider datset for NYC region and other corresponding datasets of user interviews and product marketing and engineering related events. ")
    st.write("Personal Goal: ")
    
    st.markdown('## I - Discovery')
    st.write("This part is about leveraging the insights from the data to understand the macrotrends. The questions to address from a MVP build pov are 1. Which locations do we launch the services and 2. What times should the service be available. These questions will be answered by exploring both the qualitative and quantitative data. All of the workings you see pertaining to this section are marked with the Roman Numeral - 'I' on the sidebar ")

    st.markdown('## II - Experiments and testing ')
    # st.write("Finalize the early direction for MVP from the analytical assessment & stakeholder inputs for Stage I of MVP. The early launch mapped to OKR's will help one experiment by releasing couple of options call the process - A/B Testing or even perform a variety of experiments keeping the control group in check called the multivariate testing. Here is the deep dive or evaluating the microtrends of the running experiments")
    
    # st.markdown('## III - Instrumentation | Informing data Infrastructure decisions')
    # st.write("")

    # st.markdown('## IV - Design | Results of the Iterative Product Development')

    st.write("Upcoming")
    # st.markdown("### Note:")
    
    
    st.markdown("### Resources:")
    # st.write("Check `Medium article` for Part I of the approach to building a basic data product.")
    st.write("Check `README.md` for references / resources used to build this dashboard.")
    
    
    st.write("Made by [Shweta Narendernath](https://www.shwetanarendernath.com)")