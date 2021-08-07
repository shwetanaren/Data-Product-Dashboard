import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import pydeck as pdk

def app():

    # LOADING DATA
    DATE_TIME = "pickup_datetime"
    DATA_URL = (
        "../data/concise_joined_innyc_p.csv"
    )

    @st.cache(persist=True)
    def load_data(nrows):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis="columns", inplace=True)
        data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
        return data

    data = load_data(25000)

    # CREATING FUNCTION FOR MAPS

    def map(data, lat, lon, zoom):
        st.write(pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=data,
                    get_position=["pickup_longitude", "pickup_latitude"],
                    radius=100,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
            ]
        ))

    # LAYING OUT THE TOP SECTION OF THE APP
    row1_1, row1_2 = st.beta_columns((2,3))

    with row1_1:
        st.title("Ridesharing Data")
        hour_selected = st.slider("Select hour of pickup", 0, 23)

    with row1_2:
        st.write(
        """
        ##
        Examining how Taxi pickups vary over time in New York City's and at its major regional airports.
        Use the Slider on the left to view different slices of time and explore different transportation trends.
        """)


    # FILTERING DATA BY HOUR SELECTED
    data = data[data[DATE_TIME].dt.hour == hour_selected]

    # LAYING OUT THE MIDDLE SECTION OF THE APP WITH THE MAPS
    row2_1, row2_2, row2_3 = st.beta_columns((2,1,1))

    # SETTING THE ZOOM LOCATIONS FOR THE AIRPORTS
    la_guardia= [40.7900, -73.8700]
    jfk = [40.6650, -73.7821]
    zoom_level = 12
    midpoint = (np.average(data["pickup_latitude"]), np.average(data["pickup_longitude"]))

    with row2_1:
        st.write("**All New York City from %i:00 and %i:00**" % (hour_selected, (hour_selected + 1) % 24))
        map(data, midpoint[0], midpoint[1], 11)

    with row2_2:
        st.write("**La Guardia Airport**")
        map(data, la_guardia[0],la_guardia[1], zoom_level)

    with row2_3:
        st.write("**JFK Airport**")
        map(data, jfk[0],jfk[1], zoom_level)
    


    # FILTERING DATA FOR THE HISTOGRAM
    filtered = data[
        (data[DATE_TIME].dt.hour >= hour_selected) & (data[DATE_TIME].dt.hour < (hour_selected + 1))
        ]

    hist = np.histogram(filtered[DATE_TIME].dt.minute, bins=60, range=(0, 60))[0]

    chart_data = pd.DataFrame({"minute": range(60), "pickups": hist})
    
    # LAYING OUT THE HISTOGRAM SECTION

    st.write("")

    st.write("**Breakdown of rides per minute between %i:00 and %i:00**" % (hour_selected, (hour_selected + 1) % 24))

    st.altair_chart(alt.Chart(chart_data)
        .mark_area(
            interpolate='step-after',
        ).encode(
            x=alt.X("minute:Q", scale=alt.Scale(nice=False)),
            y=alt.Y("pickups:Q"),
            tooltip=['minute', 'pickups']
        ).configure_mark(
            opacity=0.5,
            color='red'
        ), use_container_width=True)


