import os
import algo1
import linkedlist
import trie
import pickle
import sys

def main(argv):

    #Creates the index with all the words in the documents and the number of repetitions in each document
    def create(Carpeta):
        T = trie.Trie()
        Biblioteca=llenarTrie(T,Carpeta)
        with open("libreria","wb") as lib:
            sys.setrecursionlimit(2000)
            pickle.dump(Biblioteca,lib)
        print("library created successfully")
        return Biblioteca


    #Put all the words of the documents inside the trie
    def llenarTrie(T,Carpeta):
        Docs = os.listdir(Carpeta)
        #Go through all the documents
        for x in range(len(Docs)):
            with open(Carpeta + "/" + Docs[x],encoding="utf8") as Doc:
                Lines = Doc.readlines()
            #Scroll through all lines of the document
            for y in range(len(Lines)):
                Line = algo1.String(Lines[y])
                start = 0
                #Goes through all the words within the line and inserts them in the trie
                for z in range(len(Line)):
                    if Line[z] == " " or z == len(Line)-1:
                        name_document= Docs[x]
                        Word = algo1.substr(Line,start,z)
                        start =  z + 1
                        trie.insert(T,Word,name_document)
        return T            


    #Look at the keyword in the docs               
    def search (Key_word):
        with open('libreria', 'br') as lib:
            T = pickle.load(lib)
        if T == None: #First check that the trie is not empty
            print ('Error empty trie')
            return None
        if Key_word == '' :
            return None
        L = trie.search(T,Key_word) #Search in the Trie and return a list with the documents and how many times the word is repeated in each one
        if L == None:              
            print ("no document found")
            return None
        else:
            L=linkedlist.Mergesort(L) #Sort the list from highest to lowest according to relevance 
            currentnode = L.head 
            print("RESULTS:")
            while currentnode != None : #Print the list
                print (currentnode.document,', The word was found ',currentnode.value, ' times.')
                currentnode = currentnode.nextNode

    if sys.argv[1] == "-create":
        if len(sys.argv) > 3:
            print("The address must not contain spaces")
            return None
        create(sys.argv[2])
    elif sys.argv[1] == "-search":
        if len(sys.argv) > 3:
            print("Only one word can be searched")
            return None
        search(sys.argv[2])
        
if __name__ == "__main__":
    main(sys.argv[1:])
