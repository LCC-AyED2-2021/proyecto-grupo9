
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
   
#Agrega un nodo al fina de la lista
def addFinal(L,element):
    if element == None or L == None: 
        print("No se recibio nigun elemento o lista")
        return 
    newNode = Node()
    newNode.value = element
    if L.head == None: 
        L.head = newNode
    else:  
        Recorrido = L.head
        while Recorrido.nextNode != None:
            Recorrido = Recorrido.nextNode
        Recorrido.nextNode = newNode
