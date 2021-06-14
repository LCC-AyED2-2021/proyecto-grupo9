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
  for x in range(len(Docs)):
      with open(Carpeta + "/" + Docs[x],encoding="utf8") as Doc:
        Lines = Doc.readlines()
        #Recorremos todas las lineas dentro del documento
        for y in range(len(Lines)):
          Line = algo1.String(Lines[y])
          start = 0
          #Recorremos todas las palabras dentro de la linea y las insertamos en el trie
          for z in range(len(Line)):
            if Line[z] == " " or z == len(Line):
              Word = algo1.substr(Line,start,z)
              start =  z + 1
              trie.insert(T,Word,Doc)
  return T            

#----------------------------------------------------------
#agregado necesita ser arrreglado y revisado
               
def search (T,Key_word):
  L=None
  if T == None: # 1ro comprueba que el trie no este vacio 
    print ('Error trie vaccio')
    return
  start=0
  if Key_word == '' :
      return None
  L = trie.search(T,Key_word) 
  if L == None:              
    print ('"no document found"')
  else:
    L=linkedlist.Mergesort(L)
    currentnode = L.head 
    while currentnode != currentnode.nextNode:
      print (currentnode.document,' ; ',currentnode.value)
         
