import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from sympy import *
import annotated_text
nltk.download("punkt")

#ahora tienes que hacer un sistema que permita transformar de numero escrito a texto, no va a ser muy complicado,
#sigue el plan que tienes en mente, usar solamente las primeras letras para identificar completamente, es el mejor
#sistema y evita gran parte del error humano.


class formatter:
  
  def __init__(self,input):
    ordinal = {"cuadrada":"2","cubica":"3","segunda":"2","tercera":"3","cuarta":"4","quinta":"5","sexta":"6","septima":"7","octava":"8",
          "novena":"9","decima":"10"}
    replace = {"á":"a","é":"e","í":"i","ó":"o","ú":"u"}
    units = {"uno":"1","dos":"2","tres":"3","cuatro":"4","cinco":"5","seis":"6","siete":"7","ocho":"8","nueve":"9","diez":"10",
                "once":"11","doce":"12","trece":"13","catorce":"14","quince":"15","dieciseis":"16","diecisiete":"17","dieciocho":"18",
                "diecinueve":"19","veinte":"20","veintiuno":"21","veintidos":"22","veintitres":"23","veinticuatro":"24",
                "veinticinco":"25","veintiseis":"26","veintisiete":"27","veintiocho":"28","veintinueve":"29"}
    tens = {"treinta":"30","cuarenta":"40","cincuenta":"50","sesenta":"60","setenta":"70","ochenta":"80","noventa":"90"}
    hundreds = {"ciento":"100","doscientos":"200","trescientos":"300","cuatroscientos":"400","quinientos":"500","seiscientos":"600",
                    "setecientos":"700","ochocientos":"800","novecientos":"900"}
    beyond = {"mil":"1000","millon":"1000000","millones":"1000000","billones":"1000000000000","trillones":"1000000000000000000"}
    identity = (beyond,hundreds,tens,units)
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
    else:
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
imprime=str(calculator(texto))
imprime
tremendo = sympify(imprime,evaluate=False)
tremendo
resultado=N(tremendo)
resultado

