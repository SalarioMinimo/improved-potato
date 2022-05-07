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
      st.subheader("Aquí está toda la información que necesitas para hablar ecuaciones.")
      
      B_Selection = st.radio("Selecciona un apartado",("Justificación", "Ejemplos" ,"Comandos"))
      selection[B_Selection]()

  def Justificación(self):
    with st.sidebar:
     st.caption("-----")
     st.subheader("Más humano")
     st.markdown("Entre más parecido es un sistema simbólico al lenguaje natural, es mejor, puesto que utilizarlo será más parecido a hablar y como humanos somos expertos en ello.")
     st.markdown("Por esa razón elaboré un traductor-calculadora, la cual toma un texto con una sintaxis que aunque no es flexible como el lenguaje natural, si utiliza una representación simbólica muy familiar con una estructura más amigable para ser escrito en una sola linea.")
     st.markdown("En esta primera iteración del programa, solo ataca los aspectos básicos de representar la aritmetica, con un pequeño corrector de textos, pero es suficiente para llevar a cabo operaciones basntante complejas.")
     st.markdown("El siguiente paso sería hacer un speech-to-text hecho a la medida con las necesidades del programa y mejorar la sintaxis que utiliza.")
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
    for x in replace:
      self.text = self.text.replace(x,replace[x])
    
    to_correct = word_tokenize(self.text)
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

