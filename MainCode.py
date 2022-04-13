import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
import math
import sympy
nltk.download("punkt")

class calculator:
  
  def __init__(self,input):
    
    
    self.send = ""
    self.text=word_tokenize(input)
    self.functions = {"más":self.mas,"menos":self.menos}
    
    
    for x in range(len(self.text)):
      
      if self.text[x] in self.functions:
        self.functions[self.text[x]](x)
    
  def mas(self,index):
    self.text[index]="+"
    
  def menos(self,index):
    self.text[index]="-"
  
  def __str__(self):
    return TreebankWordDetokenizer().detokenize(self.text)
 
  

resultado = sympy.symbols("resultado")
texto=st.text_area(label="muerte al capital")
tremendo = str(calculator(texto))

result = sympy.solve(tremendo + (" -resultado"), resultado)



result[0]
st.latex(sympy.sympify(tremendo)
  
