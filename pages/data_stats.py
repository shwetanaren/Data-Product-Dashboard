import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

def app():
    st.title('Temporal Analysis')
    st.header("Analysing the trend of trip bookings across time slices.")
    

    # LOADING DATA
    DATE_TIME = "pickup_datetime"
    DATA_URL = (
        "../data/3_df_sort_datetime_set.csv"
    )

    @st.cache(persist=True)
    def load_data(nrows):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis="columns", inplace=True)
        data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
        return data

    data = load_data(15000)

    # LAYING OUT THE TOP SECTION OF THE APP
    
    st.write("Daily rides trend from 1st January 2016 to midnight of 1st July 2016")
    
    line = alt.Chart(data).transform_window(
        cumulative_count="count()",
        ).mark_line().encode(
        x="dates:T",
        y="count()"
        ).properties(
        width=1100,
        height=400
        )
    
    st.write(line) #use_container_width=True

    # LAYING OUT THE MIDDLE SECTION OF THE APP

    st.write("Density of trips between 1st January 2016 to midnight of 1st July 2016")

    row1_1, row1_2 = st.beta_columns((1,1))

    with row1_1:
        st.write("**Trips per month**")
        st.altair_chart(alt.Chart(data)
        .mark_area(
                interpolate='step-after',
            ).encode(
                x=alt.X("month_name:O"),
                y='count()',
                # tooltip=['minute', 'pickups']
            ).configure_mark(
                opacity=0.5,
                color='yellow'
            ).properties(
            width=450,
            height=400
            ))
        

    with row1_2:
        st.write("**Trips per weekday**")
        st.altair_chart(alt.Chart(data)
        .mark_area(
                interpolate='step-after',
            ).encode(
                x=alt.X("day_name:O", scale=alt.Scale(nice=False)),
                y='count()',
                # tooltip=['minute', 'pickups']
            ).configure_mark(
                opacity=0.5,
                color='red'
            ).properties(
            width=450,
            height=400
        ))    


    
    st.write("**Trips by the Day**")
    st.altair_chart(alt.Chart(data)
    .mark_area(
            interpolate='step-after',
        ).encode(
            x=alt.X("day:Q", scale=alt.Scale(nice=False)),
            y='count()',
            # tooltip=['minute', 'pickups']
        ).configure_mark(
            opacity=0.5,
            color='yellow'
        ).properties(
        width=1100,
        height=400
        ))                


    st.write("**Trips by the Hour**")
    st.altair_chart(alt.Chart(data)
    .mark_area(
            interpolate='step-after',
        ).encode(
            x=alt.X("hour:Q", scale=alt.Scale(nice=False)),
            y='count()',
            # tooltip=['minute', 'pickups']
        ).configure_mark(
            opacity=0.6,
            color='red'
        ).properties(
        width=1100,
        height=400
        ))    


    st.header('Analyse the distribution of pickups plotting in a daily hourwise mapping ')

    # st.selectbox('Select', ['Weekend', 'Weekday'])


    st.altair_chart(alt.Chart(data)
    .mark_rect()
    .encode(
        alt.X('day:O', title='date'),
        alt.Y('hour:O', title='hour of day'),
        alt.Color('count()', title='Densitymap of hour-day counts')
    )
    .properties(
        width=1100,
        height=800
        ))