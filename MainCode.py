import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")
  
class calculator:
  
  def __init__(self):
    self.text = "2 más 2"
    self.text = word_tokenize(self.text)
    capitalismo()
  
  def capitalismo(self):
    st.text(self.text)
    st.title("it works")
    
-calculator
