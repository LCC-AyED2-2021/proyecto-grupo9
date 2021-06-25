class LinkedList:
    head = None
    end_node = None
class Node: 
    nextNode = None
    value = None
    document = None
    
#Input: a linkedlist, a value and a document 
#Output: linkedlist
def add(L, element, document):
    if element == None or document == None:
        print("No document or item was received")
        return None
    else:
        newNode = Node()
        newNode.nextNode = L.head
        newNode.value = element
        newNode.document = document
        L.head = newNode
        return L
   
#Add a node in the end of the list
def addFinal(L,element):
    if element == None or L == None: 
        print("No item or list was received")
        return None
    newNode = Node()
    newNode.value = element
    if L.head == None: 
        L.head = newNode
        L.end_node = L.head
    else:  
        L.end_node.nextNode = newNode
        L.end_node=L.end_node.nextNode
        
#Length counts how many elements a linkedlist has
def length (L):
	currentnode = L.head
	cont = 0
	while currentnode != None:	
		cont = cont + 1
		currentnode = currentnode.nextNode
	return(cont)

#Sorting algorithm that sorts the lists from highest to lowest relevance
def Mergesort(L):
	left = LinkedList()
	right = LinkedList()
	result = LinkedList()
	longitud = length(L)
	#If the list has a length equal to or less than 1 it is not necessary to sort it
	if longitud <= 1:
		return (L)
	else:
		mitad = longitud // 2
		cont = 0
		currentnode = L.head
		#The list is split in half
		while currentnode != None:
			if cont < mitad:
				add(left,currentnode.value,currentnode.document)
			else:
				add(right,currentnode.value,currentnode.document)
			cont = cont + 1
			currentnode = currentnode.nextNode
		#Both halves are recursively traversed, splitting in two until there is only one node left in each half
		left = Mergesort(left)
		right = Mergesort(right)
		#The following lines of code prevent progress if you do not have a left and a right
		if left == None:
			return(right)
		if right == None:
			return(left)
		#When we have a right and a left we join them if and only if left and right are ordered
		currentleft = left.head
		if left.head != None and right.head != None:
			while currentleft.nextNode != None:
				currentleft = currentleft.nextNode 
			if currentleft.value >= right.head.value:
				currentleft.nextNode = right.head
				return (left)
		#If left and right are not ordered, merge is used to order them
		result = merge(left, right)
		return (result)

def merge(left, right):
	result = LinkedList()
	currentresult = Node()
	currentresult = result.head
	#Here the elements of the left and right lists are eliminated and placed in an orderly way in the result list
	while length(left) > 0 or length(right) > 0:
		if left.head != None and right.head != None:
			if left.head.value >= right.head.value:
				if  result.head == None :
					a = left.head.nextNode
					left.head.nextNode = None
					result.head = left.head		
					left.head = None
					left.head = a
					currentresult = result.head
				else:		
					a = left.head.nextNode
					left.head.nextNode = None
					currentresult.nextNode = left.head		
					left.head = None
					left.head = a
					currentresult = currentresult.nextNode
			else:
				if result.head == None :
					a = right.head.nextNode
					right.head.nextNode = None
					result.head = right.head	
					right.head = None
					right.head = a
					currentresult = result.head
				else:
					a = right.head.nextNode
					right.head.nextNode = None
					currentresult.nextNode = right.head	
					right.head = None
					right.head = a
					currentresult = currentresult.nextNode

		if length(left) > 0  and right.head == None:
			a = left.head.nextNode
			left.head.nextNode = None
			currentresult.nextNode =left.head	
			left.head =None
			left.head = a
			currentresult = currentresult.nextNode

		if length(right) > 0 and left.head == None:		
			a = right.head.nextNode
			right.head.nextNode = None
			currentresult.nextNode = right.head		
			right.head =None
			right.head = a
			currentresult = currentresult.nextNode
	return result
