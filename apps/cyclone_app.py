import pickle
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
with open("Trained_model.sav","rb") as a:
   loaded_model=pickle.load(a)
def app():
                  
                  
                   def pred_and_plot(model, filename):
                       
                     # Make a prediction
                       pred = model.predict(filename)
                       return pred
                    
                  
                   st.markdown('''<font size="42"> <b>**Get cyclone intensity with the click of a button.**</b></font>''',unsafe_allow_html=True)
    
                   file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
                  
                   if file is not None:
                      image = Image.open(file)
                  
                      st.image(
                          image,
                          caption=f"You amazing image has shape",
                          use_column_width=True,
                      )
                      img_array = np.array(image)
                      img = tf.image.resize(img_array, size=(256,256))
                      img = tf.expand_dims(img, axis=0)
                      img=img/255.
                      if st.button('Compute Intensity'):
                        intensity=pred_and_plot(loaded_model,img)
                        st.markdown("The intensity of your image in KNOTS is 👇")
                        st.success(intensity)
                 

  