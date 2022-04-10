import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")

input = "dos más dos"

input = word_tokenize(input)

input
