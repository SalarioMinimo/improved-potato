import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")


fuctions = {más:"+"}
equation = ""

input = "dos más dos"

input = word_tokenize(input)

for x in input:
  equation += x

traslator()
