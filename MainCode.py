import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from sympy import *
import annotated_text
from spellchecker import SpellChecker
nltk.download("punkt")

class side_bar:
 
  def __init__(self):
    with st.sidebar:
      selection = {"Justificación":self.Justificación,"Comandos":self.Comandos,"Ejemplos":self.Ejemplos}
      st.title("Manual de uso")
      st.subheader("Aquí está toda la información que necesitas para comenzar.")
      
      B_Selection = st.radio("Selecciona un apartado",("Justificación", "Ejemplos" ,"Comandos"))
      selection[B_Selection]()

  def Justificación(self):
    with st.sidebar:
     st.caption("-----")
     st.subheader("Más humano")
     st.markdown("Entre más parecido es un sistema simbólico al lenguaje natural, es mejor, porque su uso será casi tan sencillo como el mero acto de hablar.")
     st.markdown("Por esa razón elaboré un traductor-calculadora, la cual toma un texto con una sintaxis estricta con el fin de evitar ambigüedades, pero a su vez utiliza palabras y símbolos lingüísticos que ya conocemos, además de una estructura más amigable y familiar para ser escrita en una sola línea.")
     st.markdown("Esta primera iteración del programa abarca los aspectos básicos de la aritmética, lo que permite llevar a cabo los principales tipos de operaciones matemáticas utilizadas en diversas disciplinas.")
     st.markdown("El siguiente paso sería elaborar una función  speech-to-text hecho a la medida con las necesidades del programa y perfeccionar la sintaxis que maneja.")
     st.markdown("En esta barra hay una pequeña guia con las funciones que esta calculadora tiene y ejemplos de lo que es capaz de hacer.")

    
  def Ejemplos(self):
    with st.sidebar:
     st.markdown("-----")
     st.title("Pruebas de funcionamiento")
     st.subheader("¿De qué es capaz esta calculadora?")
     st.markdown("Ctrl + C y Ctrl + V")

  def Comandos(self):
    st.markdown("uwu")











class str_formatter:

  def __init__(self,input):
    
    ordinal = {"cuadrada":"2","cubica":"3","segunda":"2","tercera":"3","cuarta":"4","quinta":"5","sexta":"6","septima":"7","octava":"8",
          "novena":"9","decima":"10"}
    replace = {"á":"a","é":"e","í":"i","ó":"o","ú":"u"}
    
    self.text = input.lower()
    for x in range(len(self.text)):
    if self.text[x]==".":
      self.text[x]=";"
    for x in replace:
      self.text = self.text.replace(x,replace[x])
    to_correct = word_tokenize(self.text)
    st.text(to_correct)
    
    sentence = []
    for x in range(len(to_correct)):
      sentence.append(to_correct[x])

    spell = SpellChecker(language=None, case_sensitive=True)
    spell.word_frequency.load_text_file('Dictionary.txt')
    corrections = spell.unknown(sentence)
    for word in corrections:
      self.text = self.text.replace(word,spell.correction(word))
    st.text(corrections)
   
    for x in ordinal:
      self.text = self.text.replace(x,ordinal[x])
    




  def __str__(self):
    st.text(self.text)
    return self.text
    
class calculator:
  
  def __init__(self,input):
    
    self.send = ""
    self.text=word_tokenize(input)
    self.functions = {"mas":self.mas, "menos":self.menos, "por":self.por, "sobre":self.sobre, "raiz":self.raiz, "seno":self.trig,
                      "coseno":self.trig, "tangente":self.trig, "arcoseno":self.trig, "arcocoseno":self.trig, "arcotangente":self.trig,
                     "entre":self.entre,"conjunto":self.conjunto,"elevado":self.elevado,"fraccion":self.fraccion}
    self.trigonometric = {"seno":"sin","coseno":"cos","tangente":"tan","arcoseno":"asin","arcocoseno":"acos","arcotangente":"atan"}
    self.references = ("seno","coseno","tangente","arcoseno","arcocoseno","arcotangente","raiz","elevado","fraccion")
    for x in range(len(self.text)):
      if self.text[x]==",":
        self.text[x]="."
    c = -1 
    while True:
      try:
        c += 1
        if self.text[c] in self.references:
          counter += 1
        elif self.text[c] == ",":
          counter -= 1
        elif self.text[c] == ";":
          self.text[c] = ","
          for x in range(counter-1):
            self.text.insert(c,",")
            
        
        
     
    c = -1
    while True:
      try:
        c+=1
        if self.text[c] in self.functions:
          self.functions[self.text[c]](c)
          c = -1
      except:
        break
    
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
    self.text.insert(index+panner+1,"(")
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
    
  def fraccion(self,index):
   self.text[index] = "("
   self.text[index+1] = "("
   panner=0
   while True:
     if not self.text[index+panner] == "y":
       panner += 1
     else:
       break
   self.text[index+panner] = "/"
   self.text.insert(index+panner,")")
   self.text.insert(index+panner+2,"(")
   index = index + panner + 2 
   
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
   self.text[index+panner] = ")"
   self.text.insert(index+panner,")")
    
  def elevado(self,index):
    del self.text[index]
    self.text[index] = "**"
    counter = 1
    panner= 0
    while counter != 0:
      panner += 1
      if self.text[index+panner] in self.references:
        counter += 1
      if self.text[index+panner] == ".":
        counter -= 1
    self.text[index+panner]=")"
    self.text[index+1] = "("
   

  def sobre(self,index):
    self.text[index]="/"
    self.text.insert(index-1,"(")
    self.text.insert(index+3,")")
  
  def raiz(self,index):
    self.text[index]="root"
    counter = 1
    panner= 0
    while counter != 0:
      panner += 1
      if self.text[index+panner] in self.references:
        counter += 1
      if self.text[index+panner] == ".":
        counter -= 1
    self.text[index+panner]=","
    self.text.insert(index+panner+1,self.text[index+1])
    del self.text[index+1]
    self.text[index+1] = "("
    self.text.insert(index+panner+1,")")
     
  def trig(self,index):
    self.text[index] = self.trigonometric[self.text[index]]
    self.text[index+1] = "("
    counter = 1
    panner = 0
    while counter != 0:
      panner += 1
      if self.text[index+panner] in self.references:
        counter += 1
      if self.text[index+panner] == ".":
        counter -= 1
    self.text[index+panner] = ")"
    
  def conjunto(self,index):
    self.text[index] = "("
    counter = 1
    panner = 1
    if self.text[index+1] == "de":
      del self.text[index+1]
    while counter != 0:
      if self.text[index+panner] in self.references:
        counter += 1
      if self.text[index+panner] == ".":
        counter -= 1
      panner += 1
    self.text[index+panner-1] = ")"
    
  
  def __str__(self):
    self.text = TreebankWordDetokenizer().detokenize(self.text)
    return self.text
 

Documentación = side_bar()
texto=st.text_input(label="Escribe tu ecuación.")
texto = str(str_formatter(texto))
st.subheader(texto)
imprime=str(calculator(texto))
imprime
tremendo = sympify(imprime,evaluate = false)
tremendo
resultado=N(tremendo)
resultado

