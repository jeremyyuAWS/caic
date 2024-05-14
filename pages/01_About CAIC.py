import streamlit as st

col1,col2 = st.columns([0.3,0.7])
with col1:
    st.image('images/CAIC logo.png')
st.write('')
with st.expander('**About**'):
    st.markdown('''
The Colorado Avalanche Information Center (CAIC) is a program within the Colorado Department of Natural Resources, Executive Director’s Office. The program is a partnership between the Department of Natural Resources (DNR), Department of Transportation (CDOT), and the Friends of the CAIC (FoCAIC) a 501c3 group. The mission of the CAIC is to provide avalanche information, education and promote research for the protection of life, property and the enhancement of the state’s economy.
''')
st.write('')
with st.expander('**History**'):
    st.markdown('''
Since 1950 avalanches have killed more people in Colorado than any other natural hazard, and in the United States, Colorado accounts for one-third of all avalanche deaths. The Colorado Avalanche Warning Center began issuing public avalanche forecasts in 1973 as part of a research program in the USDA-Forest Service Rocky Mountain Research Station. The program moved out of the federal government and into the Colorado state government, becoming part of the Department of Natural Resources in 1983. The CAIC joined the Colorado Department of Transportation’s highway safety program in 1993. The Friends of the CAIC (a 501c3 group) formed in 2007 to promote avalanche safety in Colorado and support the recreation program of the CAIC.
''')