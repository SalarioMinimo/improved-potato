import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")
  
def capitalism():
  print("Gimme your human rights")
  
functions = {"más":capitalism}
numbers = {"dos":"2"}

equation = ""

input = "2 más 2"

input = word_tokenize(input)

functions[más]

