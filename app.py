import streamlit as st
from multiapp import MultiApp
from apps import home, cyclone_app,dataset # import your app modules here

app = MultiApp()

st.title("CycloNet")
st.markdown(f'''
   <style>
   .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2020/05/17/17/15/tornado-5182693_1280.jpg");
             background-attachment: fixed;
             background-size: cover
             }}
   </style>''',unsafe_allow_html=True)
st.markdown('''<font size="4">This is a Cyclone Intensity Estimation app using Deep Learning with just one click.This app is developed by [Sparsh Jain](https://github.com/Sparshj8287). This app is created on [Streamlit](https://docs.streamlit.io/).</font>''',unsafe_allow_html=True)

# Add all your application here
app.add_app("Introduction to app", home.app)
app.add_app("Dataset", dataset.app)
app.add_app("Cyclone Intensity Estimation using Deep Learning", cyclone_app.app)

# The main app
app.run()