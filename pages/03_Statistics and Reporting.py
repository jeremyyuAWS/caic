from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")
col1,col2 = st.columns([0.3,0.7])
with col1:
    st.image('images/CAIC logo.png')
with col2:
    st.markdown("#### The mission of the CAIC is to provide avalanche information, education, and promote research for the protection of life, property, and the enhancement of the state’s economy.")


# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")


# Import your data
df = pd.read_excel('https://avalanche.state.co.us/sites/default/files/2023-11/CAIC_Accident_Data_2023.xlsx', sheet_name='Data')
df = df.groupby(['AvyYear','State','Setting','PrimaryActivity','TravelMode']).sum(numeric_only=True)[['Killed']].reset_index()
df = df.rename(columns={'AvyYear': 'Year', 
                        'MM': 'Month',
                        'PrimaryActivity':'Primary Activity',
                        'TravelMode':'Travel Mode'
                       })
# df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(day=1))
# myyears = list(set(df['Year']))
# year = st.selectbox('Select year', myyears)
# df2 = df[df['Year']==year]
st.subheader('Avalanche Accident Data 1952-2023', divider='rainbow')
st.markdown('**Source**: Data based on [CAIC Accident Data 2023](https://avalanche.state.co.us/accidents/statistics-and-reporting)')
fig = px.scatter(df, y='State', x='Year', animation_frame='Travel Mode', color='Primary Activity',
                 size="Killed", width=1200, height=700)
st.plotly_chart(fig)

df2 = df.groupby(['Year']).sum(numeric_only=True)[['Killed']].reset_index()
fig2 = px.bar(df2, x="Year", y='Killed', width=1200, height=700, title='Avalanche Deaths by Year (US - all states)')
st.plotly_chart(fig2)


st.subheader('Explore Avalanche Accident Data', divider='rainbow')
# st.write('---')
pyg_app = StreamlitRenderer(df)
pyg_app.explorer()