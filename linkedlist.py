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
        
# Lenght solo cuenta cuantos elementos tiene una linked list
def length (L): #O(f)=n
	currentnode=L.head
	cont=0
	while currentnode != None:	
		cont =cont +1
		currentnode= currentnode.nextNode
	return(cont)


"""   merge_sort  """
# algoritmo de ordenamiento para que Las listas esten ordenadas de mayor a menor
def Mergesort(L):
	left = LinkedList()
	right = LinkedList()
	result = LinkedList()
	longitud = length(L)
	#si la lista tiene una longitud igual o menor a 1 No es necesario ordenarla
	if longitud <= 1:
		return (L)
	else:
		mitad = longitud // 2
		cont=0
		currentnode=L.head
		#se recorre loda la lista partiendola a la mita (left / right)
		while currentnode != None:
			if cont < mitad:
				add(left,currentnode.value,currentnode.document)
			else:
				add(right,currentnode.value,currentnode.document)
			cont = cont +1
			currentnode= currentnode.nextNode
		#se parte en 2 hasta que quede un solo nodo en cada left y right
		left = Mergesort(left)
		right = Mergesort(right)
		# la siguientes lineas de codigo evitan que se avance si no se tiene un left y un right
		if left == None:
			return(right)
		if right == None:
			return(left)
		# cuando tenemos un right y un left los unimos si y solo si left y right estan ordenados
		currentleft=left.head
		if left.head != None and right.head != None:
			while currentleft.nextNode != None:
				currentleft=currentleft.nextNode 
			if currentleft.value >= right.head.value:
				currentleft.nextNode= right.head
				return (left)
		#si left y right no estan ordenados se utiliza merge para ordenarlos
		result = merge(left, right)
		return (result)

def merge(left, right):
	result=LinkedList()
	currentresult = Node()
	currentresult = result.head
	#aqui se eliminan los elementos de las listas left y right  y se colocan de forma ordenada en la lista result
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
	return result
