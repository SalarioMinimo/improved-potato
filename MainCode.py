import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")

texto=st.text_area(label="muerte al capital")
st.title(texto)

