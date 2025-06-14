import streamlit as st
st.title("Sentiment Analysis",anchor=False)
container1 = st.empty()
container2 = st.empty()
with container1.container():
    st.header("Twitter's Tweets",anchor=False)
    col1, col2, col3 = st.columns([5,5,5])
    with col1:
        st.metric(label="Total Tweets", value="100000")
    with col2:
        st.metric(label="Average Sentiment Score", value="-0.038")
    with col3:
        st.metric(label="Average Subjectivity", value="0.391")
    st.image("images\Figure_1.png")
    st.divider()
with container2.container():
    st.header("IMDB's Movie Reviews",anchor=False)
    col1, col2, col3 = st.columns([5,5,5])
    with col1:
        st.metric(label="Total Reviews", value="20000")
    with col2:
        st.metric(label="Average Sentiment Score", value="0.314")
    with col3:
        st.metric(label="Average Subjectivity", value="0.529")
    st.image("images\Figure_2.png",use_column_width=True)
