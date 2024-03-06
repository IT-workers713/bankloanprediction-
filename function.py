import numpy as np
import pandas as pd
import streamlit as st
import joblib
model= joblib.load('model.joblib')
colonnes= []
"""code """
def predire():
    col= np.array([])
    """les champs de dataset choisis"""
    donnees= pd.DataFrame([col],columns=colonnes)
    prediction= model.predict(donnees)[0]


    if prediction == 1:
        st.success('Vous pouvez obtenir le prêt :le pret:')
    else:
        st.error('Désolé, vous ne pouvez pas obtenir le prêt :')

