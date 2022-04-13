import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from sympy import *
nltk.download("punkt")

class calculator:
  
  def __init__(self,input):
    
    
    self.send = ""
    self.text=word_tokenize(input)
    self.functions = {"más":self.mas,"menos":self.menos,"por":self.por,"entre":self.entre,"raiz":self.raiz}
    c=1
    while c != 0:
      c = 0
      for x in range(len(self.text)):
        if self.text[x] in self.functions:
          self.functions[self.text[x]](x)
          c += 1
    
  def mas(self,index):
    self.text[index]="+"
    
  def menos(self,index):
    self.text[index]="-"
    
  def por(self,index):
    self.text[index]="*"
    
  def entre(self,index):
    self.text[index]="/"
    self.text.insert(index-1,"(")
    self.text.insert(index+3,")")
  
  def raiz(self,index):
    self.text[index]="root("
    self.text.insert(index+2,",3")
    self.text.insert(index+3,")")
    
  
    
  
  def __str__(self):
    return TreebankWordDetokenizer().detokenize(self.text)
 
  

resultado = symbols("resultado")
texto=st.text_area(label="muerte al capital")
tremendo = str(calculator(texto))

result = solve(tremendo + (" -resultado"), resultado)
sonicexe = N(result[0])

sonicexe
tremendo
result[0]
