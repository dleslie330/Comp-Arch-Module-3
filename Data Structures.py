# Implementation of data structures in Python

def driver():

    n1 = Node("Dakota")
    n2 = Node("Sarah")
    n3 = Node("Zach")
    n4 = Node("Ethan")
    n5 = Node("Levi")

    llTest = LinkedList()
    llTest.add(n1)
    llTest.add(n3)
    llTest.add(n4)
    llTest.add(n2)
    llTest.add(n5)
    llTest.add(n1)
    print("List: ", llTest)
    llTest.remove("Ethan")
    print("Removed: Ethan")
    print("New List: ", llTest)

    return None

# build a Node in Python
class Node:
    def __init__(self, val=None):
        self.val = val
        self.nextval = None

    def pointing(self, node):
        self.next = node

    
# create a linked list (No duplicate values allowed)
class LinkedList():
    def __init__(self):
        self.head = None

    def __iter__(self):
        itnode = self.head

        while itnode is not None:
            yield itnode
            itnode = itnode.nextval

    def add(self, node):
        # if linked list is empty, create the head node
        if (self.head == None):
            self.head = node
            return

        # iterate through the linked list
        for thisNode in self:
            # if the value already exists within the list, don't add it
            if (thisNode.val == node.val):
                return None
        
        # append to linked list
        thisNode.pointing(node)

    def remove(self, val):
        if (self.head == None):
            return None
        elif (self.head.val == val):
            self.head = self.head.nextval
            return
        
        for thisNode in self:
            if (thisNode.nextval is not None):
                if (thisNode.nextval.val == val):
                    thisNode.pointing(thisNode.nextval.nextval)
                    return None

    def __repr__(self):
        prntNodes = ""

        for node in self:
            prntNodes = prntNodes + node.val + ", "

        return prntNodes
        


def Stack():
    return None

def Queue():
    return None

def Array():
    return None

driver()
