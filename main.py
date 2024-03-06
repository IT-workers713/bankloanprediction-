import streamlit as st
import function
import numpy as np
import pandas as pd
import joblib
from function import predire



st.title('Peut prendre un prêt ou non :banque:')

"""
les champs de dataset soit 1 ou 2
"""



"""
les colonnes de dataset choisis
"""
predire()

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)


st.button('Prédire',on_click=prédire)
