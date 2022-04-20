import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from sympy import *
import annotated_text
nltk.download("punkt")




class formatter:
  
  def __init__(self,input):
    ordinal = {"cuadrada":"2","cubica":"3","segunda":"2","tercera":"3","cuarta":"4","quinta":"5","sexta":"6","septima":"7","octava":"8",
          "novena":"9","decima":"10"}
    replace = {"á":"a","é":"e","í":"i","ó":"o","ú":"u"}
    self.text = input.lower()
    for x in replace:
      self.text = self.text.replace(x,replace[x])
    for x in ordinal:
      self.text = self.text.replace(x,ordinal[x])
    
    
  def __str__(self):
    return self.text

class calculator:
  
  def __init__(self,input):
    
    self.send = ""
    self.text=word_tokenize(input)
    self.functions = {"mas":self.mas, "menos":self.menos, "por":self.por, "sobre":self.sobre, "raiz":self.raiz, "seno":self.trig,
                      "coseno":self.trig, "tangente":self.trig, "arcoseno":self.trig, "arcocoseno":self.trig, "arcotangente":self.trig,
                     "entre":self.entre}
    self.trigonometric = {"seno":"sin","coseno":"cos","tangente":"tan","arcoseno":"asin","arcocoseno":"acos","arcotangente":"atan"}
    self.references = ("seno","coseno","tangente","arcoseno","arcocoseno","arcotangente","raiz")
    for x in range(len(self.text)):
      if self.text[x]==",":
        self.text[x]="."
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
    #panning backwards
    counter = 0
    panner= -1
    if self.text[index+panner] == ")":
      counter = 1
      panner = -2
    while counter != 0:
      if self.text[index+panner] == ")":
        counter += 1
      if self.text[index+panner] == "(":
        counter -= 1
      panner -= 1
    self.text.insert(index,")")
    self.text.insert(index+panner,"(")
    self.text.insert(index+panner,"(")
    index += 3
    #panning forward
    counter = 0
    panner= 1
    if self.text[index+panner] in self.references:
      counter = 1
      panner = 2
    while counter != 0:
      if self.text[index+panner] in self.references:
        counter += 1
      if self.text[index+panner] == ".":
        counter -= 1
      panner += 1
    self.text.insert(index+panner,")")
    self.text.insert(index+panner,")")
    self.text.insert(index+1,"(")
    


  def sobre(self,index):
    self.text[index]="/"
    self.text.insert(index-1,"(")
    self.text.insert(index+3,")")
  
  def raiz(self,index):
    self.text[index]="root"
    counter = 1
    panner= 1
    while counter != 0:
      if self.text[index+panner] in self.references:
        counter += 1
      if self.text[index+panner] == ".":
        counter -= 1
      panner += 1
    self.text[index+panner-1]=","
    self.text.insert(index+panner,self.text[index+1])
    del self.text[index+1]
    self.text[index+1] = "("
    self.text.insert(index+panner,")")
     
  def trig(self,index):
    self.text[index] = self.trigonometric[self.text[index]]
    self.text[index+1] = "("
    counter = 1
    panner = 1
    while counter != 0:
      if self.text[index+panner] in self.references:
        counter += 1
      if self.text[index+panner] == ".":
        counter -= 1
      panner += 1
    self.text[index+panner-1] = ")"
    
  
  def __str__(self):
    return TreebankWordDetokenizer().detokenize(self.text)
 
  
texto=st.text_input(label="muerte al capital")
texto = str(formatter(texto))
texto
tremendo = sympify(calculator(texto),evaluate=False)

imprime=str(calculator(texto))
imprime
tremendo
resultado=N(tremendo)
resultado

