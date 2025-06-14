import streamlit as st
import pandas as pd
def display_twitter():
    twitter = pd.read_csv("datasets/twitter_sentiment.csv")
    st.dataframe(twitter,use_container_width=True,hide_index=True,height=700)

def display_imdb():
    imdb = pd.read_csv("datasets/imdb_sentiment.csv")
    st.dataframe(imdb,use_container_width=True,hide_index=True,height=700)

with st.sidebar:
    dataset = st.selectbox("Select a Dataset", ["Twitter","IMDB"])
container1 = st.empty()
with container1.container():
    if dataset == "Twitter":
        st.title("Twitter's Dataset")
        display_twitter()
    elif dataset == "IMDB":
        st.title("IMDB's Dataset")
        display_imdb()
