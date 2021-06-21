import linkedlist

class Trie:
    root = None
class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False
    repeat = None
    
#Delete from the word the characters that we don´t need
def deleteChar(element):
    newElement = ""
    for x in range(0,len(element)):
        #Capital letters
        if ord(element[x]) >= 65 and ord(element[x]) <= 90:
            newElement = newElement + element[x]
        #Lower letters are converted to capital letters
        elif ord(element[x]) >= 97 and ord(element[x]) <= 122:
            newElement = newElement + chr(ord(element[x]) - 32)
        #Apostrophe and dash
        elif ord(element[x]) == 39 or ord(element[x]) == 45:
            newElement = newElement + element[x]
     
    return newElement
    

#Insert new elements in the trie
def insert(T,element,document):
    #Verify if the root exist
    if T.root == None: T.root = TrieNode()
    Node = T.root
    height = 0
    element = deleteChar(element)
    Length = len(element)
    
    #Iterate while we dont reach the length of the element
    while height != Length:
        #If the first letter does not exist, we create all the levels
        if Node.children == None:
            Level = linkedlist.LinkedList()
            Tnode = TrieNode()
            Tnode.key = element[height]
            Tnode.parent = Node
            linkedlist.addFinal(Level,Tnode)
            Node.children = Level
            Node = Tnode
            height = height + 1
            
        else:
            Level = Node.children
            Node = Node.children.head
            #We search if the letter exist in the Trie or we have to add a new node
            while Node.value.key != element[height] and Node.nextNode != None:
                Node = Node.nextNode
                
            if Node.value.key == element[height]:
                Node = Node.value
                height = height + 1
                
            else:
                Tnode = TrieNode()
                Tnode.key = element[height]
                Tnode.parent = Node.value.parent
                linkedlist.addFinal(Level,Tnode)
                Node = Tnode
                height = height + 1
                
    #Assign the end of the word
    Node.isEndOfWord = True
    #assign the repetition of the word
    if Node.repeat != None: #si la lista No esta vacia se recorre la lista buscando el Nombre del documento actual
        nodeLista = Node.repeat.head
        while NodeLista != None:
            if NodeLista.document == document: #si se encuentra se le suma 1 al campo value
                NodeLista.value += 1
                return
            else: NodeLista = NodeLista.nextNode
        linkedlist.add(Node.repeat,1,document) # si no se agrega el documento
    else: NodeLista = None # si la lista esta vacia solo se le agrega el nombre del documento 
        Node.repeat = linkedlist.LinkedList()
        linkedlist.add(Node.repeat,1,document)
    

#Search elements in the trie.
def search(T,element):
    #Verify if the root exist.
    if T.root == None:
        return None
    node = T.root.children
    element = deleteChar(element)
    for height in range(0,len(element)):
        #Verify if the linkedList exist.
        if node == None:
            return None
        currentNode = node.head
        #Search for the letter through the linkedList.
        while  currentNode != None:     
            if currentNode.value.key == element[height]:
                break            
            else:
                currentNode = currentNode.nextNode
        #If the letter is not found return None.
        if currentNode == None:
            return None
        node = currentNode.value.children
    #Verify if the letter is the end of word.
    if currentNode.value.isEndOfWord == True:
        return currentNode.value.repeat 
    else:
        return None       
      
