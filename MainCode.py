import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")

texto=st.text_area(label="muerte al capital")
textito=word_tokenize(texto)

texto
textito
