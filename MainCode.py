import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")

class calculator:
  
  def __init__(self,input):
    self.send = ""
    self.text=word_tokenize(input)
    for x in self.text:
      if self.text[x] in self.functions:
        self.functions[self.text[x]](x)
    
  def más(self,index):
    self.send = self.text[x-1]+self.text[x+1]
    
  
  def __str__(self):
    return "self.send"
  
  self.functions = {}
  self


texto=st.text_area(label="muerte al capital")
tremendo = calculator(texto)

tremendo
  
