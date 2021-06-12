import dictionary

class LinkedList:
    head=None

class Node: 
    nextNode = None
    value = None
    document = None
    

#Input: Variable tipo linkelist y un value
#Output: TAD lista
def add(L, element, document):
    if element == None or document == None:
        print("No se recibio nigun documento o elemento")
        return None
    else:
        newNode = Node()
        newNode.nextNode = L.head
        newNode.value = element
        newNode.document = document
        L.head = newNode
        return L
