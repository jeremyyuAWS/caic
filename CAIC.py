import streamlit as st

col1,col2 = st.columns([0.3,0.7])
with col1:
    st.image('images/CAIC logo.png')
with col2:
    st.markdown("##### The mission of the CAIC is to provide avalanche information, education, and promote research for the protection of life, property, and the enhancement of the state’s economy.")
st.write('---')
# Add Youtube video of CAIC homepage
# st.markdown('### :star: New CAIC Homepage Overview')
with st.expander('# :star: New CAIC Homepage Overview'):
    st.video('https://www.youtube.com/watch?v=BhXaY3u93pU')


st.link_button('CAIC 22/23 Annual Report','https://support.friendsofcaic.org/pages/annual-reports', type='primary')
st.image('images/MajorChanges.png')
st.write('---')
st.image('images/AaronCarlson.png')
st.write('---')
st.image('images/EthanGreene.png')
st.write('---')
st.image('images/AvalancheAccidents.png')
st.write('---')
st.image('images/Growing Reach.png')
st.write('---')
st.image('images/Membership.png')
