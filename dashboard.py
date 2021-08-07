# from requests.api import options
# import streamlit as st
# import pandas as pd
# import numpy as np
# import requests


# # Draw a title and some text to the app:
# '''
# # Data Product Manager - Decision Dashboard

# Below results are for .
# '''


# ticker_option = add_tickerbox = st.sidebar.selectbox(
#         "Select your Ticker?",
#         ("BTCUSDT", "ETHUSDT", "DOTUSDT", "SOLUSDT",'UBER')
#         )

# st.header(ticker_option)

# # add_chartbox = st.sidebar.selectbox(
# #     "Select the chart?",
# #     ("CandleStick", "ATR", "Goldencross")
# # )

# sentiment_option = add_sentimenttracker = st.sidebar.selectbox(
#     "Select the sentiment tracker?",
#     ("wallstreetbets", "tweepy", "stocktwits")
# )

# # st.header(sentiment_option)

# with st.beta_container():
#     st.write("CandleStick chart with options to select")
#     # You can call any Streamlit command, including custom components:
#     st.bar_chart(np.random.randn(50, 3))
#     # st.write("This is outside the container")


# df = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(df.style.highlight_max(axis=0))

# if sentiment_option == "stocktwits":
#     st.subheader("Results from Stockwits")
#     symbol = st.sidebar.text_input("Symbol", value='UBER', max_chars=8)
#     pass
#     r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
    
#     data = r.json()

#     for message in data['messages']:
#         st.image(message['user']['avatar_url'])
#         st.write(message['user']['username'])
#         st.write(message['created_at'])
#         st.write(message['body'])


# if sentiment_option == "wallstreetbets":
#     st.subheader("Results from Wallstreetbets")


