import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")

class calculator:
  
  def __init__(self,input):
    self.text=word_tokenize(input)
  
  def __str__(self):
    return "uwu"
    
    


texto=st.text_area(label="muerte al capital")
tremendo = calculator(texto)

tremendo
  
