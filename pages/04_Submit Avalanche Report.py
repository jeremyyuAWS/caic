import pandas as pd
import streamlit as st
from streamlit_player import st_player

st.set_page_config(layout="wide")
col1,col2 = st.columns([0.3,0.7])
with col1:
    st.image('images/CAIC logo.png')
with col2:
    st.markdown("##### The mission of the CAIC is to provide avalanche information, education, and promote research for the protection of life, property, and the enhancement of the state’s economy.")

with st.expander('# :video_camera: VIDEO - Submitting Field Reports'):
    st.video('https://www.youtube.com/watch?v=_hQFLJNtgyE&t=15s')

st.header('Submit Avalanche Report', divider='rainbow')
st.markdown('Cracking and collapsing in the snow are indicators of avalanche danger. Tell us if you saw cracks in the snow, felt the snow collapsing under your weight, or heard whumpfing sounds in the text box below. Please include the location, aspect, and elevation of your observation.')

img1, img2 = st.columns(2)
img1.markdown('#####  Example: Cracking Snow')
img1.image('https://d1sdegrcg1ah5f.cloudfront.net/web-assets/images/ci-images/55431/recnt-2.jpg', caption='Example: Cracking snow', width=500)
with img2:
    st.markdown('##### Example: Shooting Snow')
    st_player('https://vimeo.com/369900138')

st.markdown('##### Field Report Observations')
st.text_area(label='', placeholder='Please describe the avalanche activity you observed in detail (e.g Location, aspect, and elevation are helpful)', height=250)

st.markdown('##### Cracking Snow Severity (optional)')
st.select_slider(label='', options=['Unknown','None','Minor','Moderate','Shooting'], key='cracking')

st.markdown('##### Collapsing Snow Severity (optional)')
st.select_slider(label='', options=['Unknown','None','Minor','Moderate','Rumbling'], key='collapse')


st.button('Submit Report')

st.markdown('##### Upload photo or video (optional)')
st.file_uploader(label='')
st.write('---')

st.markdown('Your Information')
st.text('''
Your report will appear under your name in the field reports section of our website. You can remain anonymous or show your report to just the
CAIC staff by selecting hide my name and/or hide my report below.
''')
info1, info2 = st.columns(2)
info1.text_input("First Name :red[*]", placeholder="e.g. John")
info2.text_input("Last Name :red[*]", placeholder="e.g. Smith")
info1.text_input("Email :red[*]", placeholder="e.g. jsmith@mail.com")
info2.text_input("Phone Number :red[*]", placeholder="e.g. (720) 555-1212")
st.markdown(''':mag_right: Your report will appear under your name in the field reports section of our website. You can remain anonymous or show your report to just the CAIC staff by checking the corresponding boxes below''')
info3, info4 = st.columns(2)
info3.checkbox('Hide my name', key='Hidename''')
info4.checkbox('Hide my report', key='Hidereport')
st.button('Submit', type='primary')

