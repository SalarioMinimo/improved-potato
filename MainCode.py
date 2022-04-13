import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
import math
import sympy
nltk.download("punkt")

class calculator:
  
  def __init__(self,input):
    
    
    self.send = ""
    self.text=word_tokenize(input)
    self.functions = {"más":self.mas}
    
    
    for x in range(len(self.text)):
      
      if self.text[x] in self.functions:
        self.functions[self.text[x]](x)
    
    
    
  def mas(self,index):
    self.text[index]="+"
    
  
  def __str__(self):
    return str(self.text)
 
  


texto=st.text_area(label="muerte al capital")
tremendo = calculator(texto)

tremendo
  
