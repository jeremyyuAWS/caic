import pandas as pd
import streamlit as st
from streamlit_player import st_player

st.set_page_config(layout="wide")
col1,col2 = st.columns([0.2,0.8])
with col1:
    st.image('https://support.friendsofcaic.org/cdn/shop/files/FriendsCAIC_Logo2020_Color-small_180x.png')
with col2:
    st.markdown('##### The mission of **Friends of CAIC** is to support avalanche forecasting and education throughout Colorado.')
st.image('images/Friends of CAIC.png')
st.image('images/Key Accomplishments.png')
st.image('images/Forecast Support.png')
st.subheader('CAIC Annual Reports', divider='rainbow')

rep1, rep2, rep3, rep4 = st.columns(4)
rep1.link_button('CAIC 22/23 Annual Report','https://support.friendsofcaic.org/pages/annual-reports', type='primary')
rep2.link_button('CAIC 21/22 Annual Report','https://cdn.shopify.com/s/files/1/0269/0924/5519/files/FoCAIC_CAIC_FY22AnnualReport.pdf?v=1679586965')
rep3.link_button('CAIC 20/21 Annual Report','https://cdn.shopify.com/s/files/1/0269/0924/5519/files/CAIC_FY21AnnualReport_Web-small.pdf')
rep4.link_button('CAIC 19/20 Annual Report','https://classic.avalanche.state.co.us/wp-content/uploads/2013/09/CAIC_FY20AnnualReport_Final_Web-large.pdfs')
rep1.link_button('CAIC 18/19 Annual Report','https://classic.avalanche.state.co.us/wp-content/uploads/2020/02/FY19AnnualReport.pdf')
rep2.link_button('CAIC 17/18 Annual Report','https://classic.avalanche.state.co.us/wp-content/uploads/2019/02/CAIC_Annual_Report_2017-18.pdf')
rep3.link_button('CAIC 16/17 Annual Report','https://classic.avalanche.state.co.us/wp-content/uploads/2013/09/FoCAIC_annual-report_16-17_final.pdf')
rep4.link_button('CAIC 15/16 Annual Report','https://classic.avalanche.state.co.us/wp-content/uploads/2013/09/caic_annual-report_15-16.pdf')





