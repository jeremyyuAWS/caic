from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
col1,col2 = st.columns([0.3,0.7])
with col1:
    st.image('images/CAIC logo.png')
with col2:
    st.markdown("##### The mission of the CAIC is to provide avalanche information, education, and promote research for the protection of life, property, and the enhancement of the state’s economy.")