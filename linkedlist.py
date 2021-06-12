import dictionary

class LinkedList:
    head=None

class Node: 
    nextNode = None
    value = None

#Input: Variable tipo linkelist y un value
#Output: TAD lista
def add(L, element):
    if element == None:
        return None
    else:
        newNode = Node()
        newNode.nextNode = L.head
        newNode.value = element
        L.head = newNode
        return L

#Add a dictionaryNode to a linkedlist
def addDictionary(L, element,key):
    if element == None or key == None or L == None: return None
    #Node = L.head
    #Verify if the key is already inside the list
    #while Node.nextNode != None:
        #if Node.key == key: return None 
    #if Node.key == key: return None
    newNode = dictionary.DictionaryNode()
    newNode.nextNode = L.head
    newNode.value = element
    newNode.key = key
    L.head = newNode
    return L

def addDictionaryWithoutRep(L,element,key):
    if element == None or key == None or L == None: return None
    newNode = dictionary.DictionaryNode()
    newNode.value = element
    newNode.key = key
    if L.head != None:
        Node = L.head
        #Verify if the key is already inside the list
        while Node.nextNode != None:
            if Node.key == key: return None 
        if Node.key == key: return None
        newNode.nextNode = L.head
    L.head = newNode
    return L

#Agrega un nodo al fina de la lista
def addFinal(L,element):
    if element == None or L == None: return 
    newNode = Node()
    newNode.value = element
    if L.head == None: 
        L.head = newNode
    else:  
        Recorrido = L.head
        while Recorrido.nextNode != None:
            Recorrido = Recorrido.nextNode
        Recorrido.nextNode = newNode



#Input: Una lista y un value
#Output: Posicion del nodo que contiene el value
def search(L, element):
    if L.head == None: #Validar entradas ## 1 OE
        return None # 2 OE
    else:
        currentNode = L.head #
        currentPos = 0 
        while currentNode != None: # O(N)
            if currentNode.value == element:
                return currentPos
            else: 
                currentNode = currentNode.nextNode
                currentPos += 1 
        return False

#Input: Una lista y un value
#Output: True o False dependiendo si se encuentra el elemento
def searchLogico(L, element):
    if L.head == None: #Validar entradas ## 1 OE
        return None # 2 OE
    else:
        currentNode = L.head #
        while currentNode != None: # O(N)
            if currentNode.value == element:
                return True
            else: 
                currentNode = currentNode.nextNode
        return False

            
#Input: Una lista, un valor y un valor de posicion
#Output: La lista con un nuevo nodo insertado en el valor de posicion y en cuyo campo value se encuentra el valor de element
# O(N)
def insert(L, element, position):
    longitud = length(L)
    if position > longitud or position < 0: #Validar entradas
        return None
    else: 
        if position == 0: #Caso excepcional
            add(L, element)
            return position
        else:   #Caso general
            currentNode = L.head
            currentPos = 0
            while currentPos != (position - 1): #Se llega hasta el nodo anterior del nodo que se encuentra en position
                currentNode = currentNode.nextNode
                currentPos += 1 
            newNode = Node()
            newNode.value = element
            newNode.nextNode = currentNode.nextNode
            currentNode.nextNode = newNode
            return position 

#Input: Una lista.
#Output: cantidad de elementos activos de esa lista.
# O(n)
def length(L):
    if L.head == None: 
        return 0
    else: 
        currentNode = L.head
        longitud = 0
        while currentNode != None: 
            longitud += 1
            currentNode = currentNode.nextNode
        return longitud

# Input Una lista y una variable
# Ouput La lista con el nodo.value que coincide con element desvinculado
# O(c) c∈R
def deleteElement(L, element): #Funcion wrapper
    if L.head == None: #Validar entradas
        return None
    elif L.head.value == element :
        L.head = L.head.nextNode
        return 0
    else:
        currentNode = L.head
        return deleteElementRecursive(L, element, currentNode, 1) #Funcion recursiva 

# Input Una lista, un valor element, un puntero y la posicion del mismo
# Ouput Valor de posicion del puntero en el momento que se desvincula un nodo de la lista
# O(log (n))
def deleteElementRecursive(L, element, currentNode, currentPos): 
    if currentNode.nextNode == None: #Caso base (No existe el elemento a eliminar dentro de la lista)
        return None
    elif currentNode.nextNode.value == element: #Caso base (el puntero apunta al nodo anterior del nodo a desvincular)
        currentNode.nextNode = currentNode.nextNode.nextNode
        return currentPos
    else:  #Caso general se avanza el puntero y la posicion del mismo
        return deleteElementRecursive(L, element, currentNode.nextNode, currentPos + 1)

#Input Una lista y un valor de posicion
#Output La lista con el nodo que se encuentra en el valor de position desvinculado
# O(c) C e R 
def deletePosition(L, position):
    if L.head == None: #Validar entradas
        return None
    else:
        longitud = length(L) - 1
        if position > longitud or position < 0: #Validar entradas  
            return None
        else:
            if position == 0: #Caso excepcional
                L.head = L.head.nextNode 
                return 0
            else: #Caso general
                return deletePositionRecursive(L, position, L.head, 0)

#Input una lista con un valor de posicion, una variable apuntador y su posicion dentro de la lista
# O(log n)
def deletePositionRecursive(L, position, currentNode, currentPos):
    if currentPos == position - 1: #Caso base
        currentNode.nextNode = currentNode.nextNode.nextNode
        return position
    else: #Caso general
        return deletePositionRecursive(L, position, currentNode.nextNode, currentPos + 1)

# Input Una lista y un valor de posicion
# Output el campo value del nodo que se encuentra en la posicion
# O(n)
def access(L,position):
    if L.head == None: #Validar entradas
        return None
    else: 
        longitud = length(L) - 1
        if position > longitud or position < 0: #Validar entradas
            return None
        else: #Caso general
            currentNode = L.head
            currentPos = 0
            while currentPos != position: 
                currentNode = currentNode.nextNode
                currentPos += 1
            return currentNode

#Input Una lista, un valor de elemento y un valor de posicion
#Output La lista con el update realizado o en caso de no ser posible, retorna vacio
# O(n)
def update(L,element,position): 
    if L.head == None: # Validar entradas
        return None
    else:
        longitud = length(L) - 1 
        if position > longitud or position < 0: #Validar entradas
            return None
        else: #Caso general
            currentNode = L.head
            currentPos = 0
            while currentPos != position:
                currentNode = currentNode.nextNode
                currentPos += 1
            currentNode.value = element
            return position

#Input Una lista, valor de posicion origen y valor de posicion destino
#Output Lista actualizada con el cambio realizado
def move(L, positionOrg, positionDest): 
    if L.head == None: #Validar entradas
        return None
    else:
        longitud = length(L) 
        if positionOrg > longitud or positionDest > longitud or positionDest < 0 or positionOrg < 0: #Validar entradas
            return None
        else:
            currentNode = L.head
            currentPos = 0
            while currentPos != positionOrg:
                currentNode = currentNode.nextNode
                currentPos += 1
            value = currentNode.value 
            deletePosition(L, positionOrg)
            insert(L, value, positionDest)
            return L

def deletePosicion(L,position):
  if L.head == None:
    return None
  currentNode = L.head
  if position == 0:
    L.head = L.head.nextNode
  for _ in range(0,position - 1):
    currentNode = currentNode.nextNode
  currentNode.nextNode = currentNode.nextNode.nextNode

#Mueve un nodo de su posicion en la lista a otra nueva poscion
def movePosicion(L,p_orig,p_dest):
  if L.head == None:
    return print("La lista esta vacia")
  currentNode = L.head
  for _ in range(0,p_orig):
    currentNode = currentNode.nextNode
  valorO = currentNode.value
  currentNode = L.head
  for _ in range(0,p_dest):
    currentNode = currentNode.nextNode
  valorD = currentNode.value
  insert(L,valorD,p_orig)
  deletePosicion(L,p_orig + 1)
  insert(L,valorO,p_dest)
  deletePosicion(L,p_dest + 1)
  return L

def printLista(L):
  tamaño = length(L)
  currentNode = L.head
  for _ in range(0,tamaño):
    print(currentNode.value)
    currentNode = currentNode.nextNode