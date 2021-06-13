import os
import algo1
import linkedlist
import trie

#Crea el indice con todas las palabras de los documentos y la cantidad de repeticiones en cada documento
def create(Carpeta):
  T = trie.Trie()
  Biblioteca=llenarTrie(T,Carpeta)
  print('"library created successful"')
  return Biblioteca
  
#Coloca todas las palabras de los documentos dentro del trie
def llenarTrie(T,Carpeta):
  Docs = os.listdir(Carpeta)
  #Recorremos todos los documentos
  for x in range(0,len(Docs)):
      with open(Carpeta + "/" + Docs[x], encoding="utf8") as Doc:
          Lines = Doc.readlines()
          #Recorremos todas las lineas dentro del documento
          for y in range(0,len(Lines)):
            Line = algo1.String(Lines[y])
            start = 0
            #Recorremos todas las palabras dentro de la linea y las insertamos en el trie
            for z in range(0,len(Line)):
              if Line[z] == " ":
                Word = algo1.substr(Line,start,z)
                start =  z + 1
                trie.insert(T,Word,Doc)
  return T  

#----------------------------------------------------------
#agregado necesita ser arrreglado y revisado
               
def search (T,Key_word):
  L=None
  if T == None: # 1ro comprueva que el trie no este vacio 
    print ('Error trie vaccio')
    return
  start=0
  for i in range(0,len(Key_word)): # este for no sirve borrar 
    if Key_word == ' ' or i+1 == len(Key_word): 
      Word = algo1.substr(Key_word,start,i)
      start = i + 1
      L = trie.search(T,Word) 
  if L == None:              
    print ('"no document found"')
  else:
    L=linkedlist.Mergesort(L)
    currentnode = L.head 
    while currentnode != currentnode.nextNode:
      print (currentnode.document,' ; ',currentnode.value)
    