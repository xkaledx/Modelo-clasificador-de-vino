# -*- coding: utf-8 -*-
"""Final (6).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hDKcSiALlUyT9lzL0kTVtqwMOgroCgt1
"""

from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np


def predict_quality(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    return predictions_data['Label'][0]
    
model = load_model('extra_tree_model')


st.title('Modelo de clasificador de vino')
st.write('Esta es una aplicación web para clasificar la calidad de su vino en función de\
         varias funciones que puede ver en la barra lateral. Por favor, ajuste el\
         valor de cada característica. Después de eso, haga clic en el botón Predecir en la parte inferior para\
         ver la predicción del clasificador.')

Acidez_fija = st.sidebar.slider(label = 'Acidez fija', min_value = 4.0,
                          max_value = 16.0 ,
                          value = 10.0,
                          step = 0.1)

volatile_acidity = st.sidebar.slider(label = 'Acidez volátil', min_value = 0.00,
                          max_value = 2.00 ,
                          value = 1.00,
                          step = 0.01)
                          
citric_acid = st.sidebar.slider(label = 'Ácido cítrico', min_value = 0.00,
                          max_value = 1.00 ,
                          value = 0.50,
                          step = 0.01)                          

residual_sugar = st.sidebar.slider(label = 'Azúcares residuales', min_value = 0.0,
                          max_value = 16.0 ,
                          value = 8.0,
                          step = 0.1)

chlorides = st.sidebar.slider(label = 'Cloruros', min_value = 0.000,
                          max_value = 1.000 ,
                          value = 0.500,
                          step = 0.001)
   
f_sulf_diox = st.sidebar.slider(label = 'Dióxido de azufre libre', min_value = 1,
                          max_value = 72,
                          value = 36,
                          step = 1)

t_sulf_diox = st.sidebar.slider(label = 'Dióxido de azufre total', min_value = 6,
                          max_value = 289 ,
                          value = 144,
                          step = 1)

density = st.sidebar.slider(label = 'Densidad	', min_value = 0.0000,
                          max_value = 2.0000 ,
                          value = 0.9900,
                          step = 0.0001)

ph = st.sidebar.slider(label = 'pH', min_value = 2.00,
                          max_value = 5.00 ,
                          value = 3.00,
                          step = 0.01)
                          
sulphates = st.sidebar.slider(label = 'Sulfatos', min_value = 0.00,
                          max_value = 2.00,
                          value = 0.50,
                          step = 0.01)

alcohol = st.sidebar.slider(label = 'Alcohol', min_value = 8.0,
                          max_value = 15.0,
                          value = 10.5,
                          step = 0.1)

features = {'fixed acidity': fixed_acidity, 'volatile acidity': volatile_acidity,
            'citric acid': citric_acid, 'residual sugar': residual_sugar,
            'chlorides': chlorides, 'free sulfur dioxide': f_sulf_diox,
            'total sulfur dioxide': t_sulf_diox, 'density': density,
            'pH': ph, 'sulphates': sulphates, 'alcohol': alcohol
            }
 

features_df  = pd.DataFrame([features])

st.table(features_df)  

if st.button('Predict'):
    
    prediction = predict_quality(model, features_df)
    
    st.write(' Based on feature values, your wine quality is '+ str(prediction))
