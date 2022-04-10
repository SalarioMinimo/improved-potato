import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")

uwu = "Los burritos son alimentos"

uwutk = word_tokenize(uwu)

uwutk
