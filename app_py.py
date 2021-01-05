# -*- coding: utf-8 -*-


# Commented out IPython magic to ensure Python compatibility.
 
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
 
st.set_option('deprecation.showfileUploaderEncoding', False)
@st.cache(allow_output_mutation = True)
 
def load_model():
    model = tf.keras.models.load_model('mobilenet.h5')
    return model
model = load_model()

page = st.sidebar.selectbox(
     "Choose a page", ['Prediction', 'Model details'])
 
if page == 'Prediction':
 
     st.header("🚀 Try it out!")
     st.write('Image Classification')
     file = st.file_uploader('Please upload an image', width = 25, type = ['jpg', 'png'])
 
     def import_and_predict(image_data, model):
       size = (160, 160)
       image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
       img = np.asarray(image)
       img_reshape = img[np.newaxis,...]
       prediction = model.predict(img_reshape)
 
       return prediction
     if file is None:
       st.text('Please upload an image')
 
     else:
       image = Image.open(file)
       st.image(image, use_column_width = True)
       prediction = import_and_predict(image, model)
       class_name = ['Parasitized', 'Uninfected']
       string = 'This image is most likely: '+class_name[np.argmax(prediction)]
       st.success(string)
       
elif page == 'Model details':
 st.write('Will be uploaded soon....')
