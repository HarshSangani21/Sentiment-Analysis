import streamlit as st
import pandas as pd

st.set_page_config("Sentiment Analysis",menu_items={"Get Help": "mailto:hharshsangani@gmail.com"})

pg = st.navigation([st.Page("page_1.py",title="Home",icon=":material/home:"), st.Page("page_2.py",title="Data Overview",icon=":material/bar_chart:"), st.Page("page_3.py",title="User Input Analysis",icon=":material/keyboard_external_input:")])
pg.run()



