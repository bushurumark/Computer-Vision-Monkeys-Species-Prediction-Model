#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install tensorflow


# In[2]:


import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the model
model = tf.keras.models.load_model('model.h5')

# Define a function to preprocess the image
def preprocess_image(image):
    image = image.resize((224, 224))  # Adjust size to match model input
    image = np.array(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = image / 255.0  # Normalize
    return image

# Define a function to make predictions
def predict(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    return prediction

# Custom CSS for background and other elements
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .title {
        color: #333;
        font-family: 'Arial';
        text-align: center;
    }
    .uploader {
        text-align: center;
    }
    .prediction {
        font-size: 20px;
        color: #4CAF50;
        font-weight: bold;
        text-align: center;
    }
    .uploaded-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border: 5px solid #ccc;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit interface with custom styles
st.markdown('<h1 class="title">Computer Vision Monkeys Species Prediction Model</h1>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True, output_format='JPEG', channels='RGB')
    st.write("")
    st.markdown('<div class="prediction">Classifying...</div>', unsafe_allow_html=True)
    prediction = predict(image)
    st.markdown(f'<div class="prediction">Prediction: {prediction}</div>', unsafe_allow_html=True)


# In[ ]:




