

class Trie:
  root = None

class TrieNode:
  parent = None
  children = None
  key = None
  isEndOfWord = False
  repeat = None
    
class repeatNode:
  repeted = None
  document = None
  nextNode = None
    
#Delete from the word the characters that we don´t need
def deleteChar(element):
  newElement = ""
  for x in range(0,len(element)):
    #Capital letters
    if ord(element[x]) >= 65 and ord(element[x]) <= 90:
      newElement = newElement + element[x]
      #Lower case
      elif ord(element[x]) >= 97 and ord(element[x]) <= 122:
        newElement = newElement + element[x]
      #Apostrophe
      elif ord(element[x]) == 39:
        newElement = newElement + element[x]
     
  return newElement

#Insert new elements in the trie
def insert(T,element):
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
                
    #Assign the end of the word and the times that word is repeted in the documents
    Node.isEndOfWord = True
    Node.repeat = linkedlist.LinkedList()
    linkedlist.add(Node.repeat,)
