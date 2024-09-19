# ===
# Code de base
# ===

class LinkedList:
    def __init__(self):
        self.premier=None
        
    def addInHead(self,Val):
        Node=Element(Val)
        Node.suiv=self.premier
        self.premier=Node
    
    def addInTail(self,Val):
        Node=Element(Val)
        current=self.premier
        while current.suiv!=None:
            current=current.suiv
        current.suiv=Node

    def inList(self):
        self.premier.printRecRev()
    
    def insertIn(self,Val):
        NewNode=Element(Val)
        if self.premier==None:
            self.premier=NewNode
        elif Val<self.premier.value:
            NewNode.suiv=self.premier
            LC.premier=NewNode
        else:
            self.premier.insertIn(NewNode)

    def impairs(self):
        if self.premier==None:
            return None
        else:
            a=self.premier
            while a.suiv!=None:
                if (a.suiv.value % 2)==0:
                    a.suiv=a.suiv.suiv
                else:
                    a=a.suiv
        self.inList()


class Element:
    def __init__(self,value):
        self.value=value
        self.suiv=None

    def printRecRev(self):
        if self.suiv==None:
            print(self.value)
            return self.value
        else:
            self.suiv.printRecRev()
            print(self.value)
        
    def insertIn(self,NewNode):
        if self.suiv==None:
            self.suiv=NewNode
        elif self.suiv.value>NewNode.value:
            NewNode.suiv=self.suiv
            self.suiv=NewNode
        else:
            return self.suiv.insertIn(NewNode)
    
             



        
N1=Element(1)
LC=LinkedList()
LC.premier=N1
LC.addInTail(10)
LC.addInTail(5)
LC.addInTail(11)
LC.addInTail(6)
LC.addInTail(2)
LC.addInTail(8)
LC.addInTail(5)


# La Linkedlist est composé de 8,4,3,2,1

# === 
# Exercice SDD
# ===

print("Attention, ma fonction pour afficher (inlist) affiche recursivement à l'envers. Donc pour 1 -> 5 -> 11 -> 5 , elle va afficher 5 -> 11 -> 5 -> 1")
LC.impairs()