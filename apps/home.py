import streamlit as st

def app():
    st.title('Introduction')
    st.write()
    st.markdown('''<p style="font-family:sans-serif; color:white; font-size: 20px;">An App User Interface where the user can upload INSAT-3D IR Satellite Image of Cyclone which is then passed to our Deep Convolutional Neural Network built in Tensorflow which is trained on Cyclone imagery of various intensities on our custom dataset curated from Raw INSAT-3D satellite captured images on MOSDAC server.
    <br>The CNN eliminates the need for usage of traditional methods for accurate center determination to estimate the Cyclone intensity using Satellite imagery.
    <br>The Model will return the estimated Intensity of satellite cyclone image in KNOTS instantly.</br></p>''',unsafe_allow_html=True)
