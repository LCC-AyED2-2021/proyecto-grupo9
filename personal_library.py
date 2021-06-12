import os
import algo1
import linkedlist
import trie

#Crea el indice con todas las palabras de los documentos y la cantidad de repeticiones en cada documento
def create(Carpeta):
  T = trie.Trie()
  llenarTrie(T,Carpeta)
 
#Coloca todas las palabras de los documentos dentro del trie
def llenarTrie(T,Carpeta):
  Docs = os.listdir(Carpeta)
    #Recorremos todos los documentos
    for x in range(len(Docs)):
      with open(carpeta + "/" + Docs[x],"r") as Doc:
        Lines = Doc.readlines()
        #Recorremos todas las lineas dentro del documento
        for y in range(len(Lines)):
          Line = algo.String(Lines[y])
          start = 0
          #Recorremos todas las palabras dentro de la linea y las insertamos en el trie
          for z in range(len(Line)):
            if Line[z] == " ":
              Word = algo.substr(Line,start,z)
              start =  z 
              trie.insert(T,Word,Doc)
            else:
              Word = algo.substr(Line,start,z)
              trie.insert(T,Word,Doc)
        
  

