import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")

texto=""
st.text_area(texto)
st.title(texto)

