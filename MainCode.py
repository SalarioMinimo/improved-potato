import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")


functions = {"más":"+"}
numbers = {"dos":"2"}
equation = ""

input = "dos más dos"

input = word_tokenize(input)

input

for x in range(len(input)):
  word = input[x]
  if word in functions:
    equation += functions[word]
  elif input[x] in numbers:
    equation += numbers[word]

equation
    
