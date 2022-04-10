import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")

def addition(n1,n2):
  return int(n1)+int(n2)
  

functions = {"más":"+"}
numbers = {"dos":"2"}
equation = ""

input = "dos más dos"

input = word_tokenize(input)

input

for x in range(len(input)):
  word = input[x]
  if word in functions:
    result = functions[word(input[x-1],input[x+1])]

result
    
