import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")

def addition(n1,n2):
  return int(n1)+int(n2)
  

functions = {"más":addition}
numbers = {"dos":"2"}

equation = ""

input = "2 más 2"

input = word_tokenize(input)

input

