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
    print (element[x], ord(element[x]))  # Eliminar (sirve para saber si la maquina sigue andando)
    #Capital letters
    if ord(element[x]) >= 65 and ord(element[x]) <= 90:
      newElement = newElement + element[x]
      #Lower case
    elif ord(element[x]) >= 97 and ord(element[x]) <= 122:
      newElement = newElement + element[x]
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
    if Node.repeat != None: NodeLista = Node.repeat.head
    else: NodeLista = None
    while NodeLista != None:
      if NodeLista.document == document: 
        NodeLista.value += 1
        return
      else: NodeLista = NodeLista.nextNode
    Node.repeat = linkedlist.LinkedList()
    linkedlist.add(Node.repeat,1,document)
    
#----------------------------------------------------------
#agregado necesita ser arrreglado y revisado  
    
def search(T,element):
  Node = T.root
  height = 0
  element = deleteChar(element)
  Length = len(element)
  while height != Length:
      if Node == None:
        return None   
      else:
        if Node.children == None:
          return None
        Level = Node.children
        Node = Node.children.head
        while Node.value.key != element[height] and Node.nextNode != None:
          Node = Node.nextNode               
          if Node.value.key == element[height]:
            Node = Node.value
            height = height + 1                
          else:
            return None
          
  return Node.repeat              