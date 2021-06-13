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
        

#ESTE ALGORITMO DE ORDENAMIENTO FUNCIONA (NO RECUERDO COMO) LO PUSE PARA VER SI REALMENTE FUNCIONA LA IMPLEMENTACION 
#DESPUES CAMBIENLO SI TIENEN UNO QUE RECUERDEN COMO FUNCIONA 

def length (L): #O(f)=n
	currentnode=L.head
	cont=0
	while currentnode != None:	
		cont =cont +1
		currentnode= currentnode.nextNode
	return(cont)


"""   merge_sort  """

def Mergesort(L):
	left = LinkedList()
	right = LinkedList()
	result = LinkedList()
	longitud = length(L)
	if longitud <= 1:
		return (L)
	else:
		mitad = longitud // 2
		cont=0
		currentnode=L.head
		while currentnode != None:
			if cont < mitad:
				add(left,currentnode.value)
			else:
				add(right,currentnode.value)
			cont = cont +1
			currentnode= currentnode.nextNode
		left = Mergesort(left)
		right = Mergesort(right)
		if left == None:
			return(right)
		if right == None:
			return(left)
		currentleft=left.head
		if left.head != None and right.head != None:
			while currentleft.nextNode != None:
				currentleft=currentleft.nextNode 
			if currentleft.value >= right.head.value:
				currentleft.nextNode= right.head
				return (left)
		result = merge(left, right)
		return (result)

def merge(left, right):
	result=LinkedList()
	currentresult = Node()
	currentresult = result.head
	while length(left)> 0 or length(right) > 0:
		if left.head != None and right.head != None:
			if left.head.value >= right.head.value:
				if  result.head== None :
					a= left.head.nextNode
					left.head.nextNode= None
					result.head=left.head		
					left.head=None
					left.head= a
					currentresult= result.head

				else:		
					a= left.head.nextNode
					left.head.nextNode= None
					currentresult.nextNode=left.head		
					left.head=None
					left.head= a
					currentresult= currentresult.nextNode

			else:
				if result.head == None :
					a= right.head.nextNode
					right.head.nextNode= None
					result.head=right.head	
					right.head=None
					right.head= a
					currentresult= result.head

				else:
					a= right.head.nextNode
					right.head.nextNode= None
					currentresult.nextNode=right.head	
					right.head=None
					right.head= a
					currentresult= currentresult.nextNode

		if length(left) > 0  and right.head== None:
			a= left.head.nextNode
			left.head.nextNode= None
			currentresult.nextNode=left.head	
			left.head=None
			left.head= a
			currentresult= currentresult.nextNode

		if length(right) > 0 and left.head== None:		
			a= right.head.nextNode
			right.head.nextNode= None
			currentresult.nextNode=right.head		
			right.head=None
			right.head= a
			currentresult= currentresult.nextNode
	return (result)