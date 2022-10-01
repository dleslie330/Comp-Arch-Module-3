# Implementation of data structures in Python

from tkinter import W

# The main driver code of the project
def driver():

    n1 = Node("Dakota")
    n2 = Node("Sarah")
    n3 = Node("Zach")
    n4 = Node("Ethan")
    n5 = Node("Levi")
    n6 = Node("Archer")

    print("LinkedList")
    llTest = LinkedList()
    llTest.append(n1)
    print(llTest)
    llTest.append(n2)
    llTest.append(n3)
    llTest.append(n4)
    llTest.append(n5)
    print(llTest)
    llTest.appbeg(n6)
    print(llTest)
    llTest.rmvbeg()
    print("removed from beginning: ", "List: ", llTest)
    n6.next = None
    llTest.append(n6)
    print(llTest)
    llTest.rmvend()
    print("removed from end: ", "List: ", llTest)

    print("\n\nStack:")
    stllTest = StackLL()
    stllTest.push(n1)
    print(stllTest)
    stllTest.push(n2)
    stllTest.push(n3)
    stllTest.push(n4)
    stllTest.push(n5)
    print(stllTest)
    stllTest.pop()
    print("pop: ", stllTest)

    print("\n\nQueue:")
    n1.next = None
    n2.next = None
    n3.next = None
    n4.next = None
    n5.next = None
    quellTest = QueueLL()
    quellTest.add(n1)
    print(quellTest)
    quellTest.add(n2)
    quellTest.add(n3)
    quellTest.add(n4)
    quellTest.add(n5)
    print(quellTest)
    quellTest.dequeue()
    print("remove: ", quellTest)

    print("\n\nArray:")
    arr = []
    arr.append(n1)
    print(arr)
    arr.append(n2)
    arr.append(n3)
    arr.append(n4)
    arr.append(n5)
    print(arr)
    print("first: ", arr[0])
    print("last: ", arr[4])
    print("size", len(arr))

    print("\n\n Array Stack")
    arrStackTest = StackA()
    arrStackTest.push("Dakota")
    print(arrStackTest)
    arrStackTest.push("Sarah")
    arrStackTest.push("Zach")
    arrStackTest.push("Ethan")
    arrStackTest.push("Levi")
    arrStackTest.push("Archer")
    print(arrStackTest)
    temp = arrStackTest.pop()
    print("pop ", temp, arrStackTest)

    print("\n\n Array Queue")
    arrQueueTest = QueueA()
    arrQueueTest.add("Dakota")
    print(arrQueueTest)
    arrQueueTest.add("Sarah")
    arrQueueTest.add("Zach")
    arrQueueTest.add("Ethan")
    arrQueueTest.add("Levi")
    arrQueueTest.add("Archer")
    print(arrQueueTest)
    temp = arrQueueTest.dequeue()
    print("Dequeue ", temp, arrQueueTest)

    return None

# Create the Node class (used to build a linked list)
class Node:
    # Initialize the node
    def __init__(self, data):
        self.data = data
        self.next = None

    # represent the node as a string (memory data isn't useful in this instance, so only the data is needed)
    def __repr__(self):
        return str(self.data)

# Create the Linked List class
class LinkedList:
    # initialize the linked list class
    def __init__(self):
        self.head = None # Know where it starts for iteration
        self.tail = None # Know where it ends for easy appending

    # Check if the list is empty
    def isEmpty(self):
        return (self.head == None)

    # add an item to the end of the list
    def append(self, data):
        # if the list is empty, make it the head of the list
        if (self.isEmpty()):
            self.head = data
            self.tail = self.head
        # Otherwise, make the current end point to the new node, and set the new node as the end
        else:
            self.tail.next = data
            self.tail = self.tail.next

    # add an item to the beginning of the list
    def appbeg(self, data):
        temp = data
        temp.next = self.head # point the new node to the current head
        self.head = temp # make new node the head

    # remove an item from the beginning of the list
    def rmvbeg(self):
        beg = self.head.data # for return data
        self.head = self.head.next # make the second item in the list the head
        return beg
    
    # remove an item from the end of the list
    def rmvend(self):
        end = self.tail.data # for return data
        temp = self.head # temporary variable for iterating through the list

        # if the list is empty, don't remove an item
        if (self.isEmpty()):
            return None

        # if there is only one item in the list, reset the list
        if (self.head.next == None):
            self.head = None
            self.tail = None
            return end
        
        # iterate through the list to find the end
        while temp.next.next is not None:
            temp = temp.next

        self.tail = temp # point the end of the list to the second to last node
        self.tail.next = None # erase the connection to the old tail
        return end
    
    # represent the data as a string
    def __repr__(self):
        rtstr = ""
        temp = self.head # temp for iterating
        while temp is not None:
            rtstr = rtstr + str(temp.data) + "->" # add each item to the string
            temp = temp.next

        return rtstr

# Create the Linked List implimentation of a Stack class
class StackLL():
    # Initialize the stack
    def __init__(self):
        self.stck = LinkedList() # Build from the linked list

    # push an item to the top of the stack
    def push(self, data):
        self.stck.appbeg(data) # use specific linked list function

    # pop an item from the top of the stack
    def pop(self):
        return self.stck.rmvbeg() # use specific linked list function

    # display the structure as a string
    def __repr__(self):
        return str(self.stck) # since the structure is a linked list, use the linked list __repr__() function

# Create an Array implementation of a Stack
class StackA():
    def __init__(self):
        self.stck = []

    def push(self, data):
        self.stck.append(data)

    def pop(self):
        return self.stck.pop()

    def __repr__(self):
        return str(self.stck)

# Create the Linked List represenation of a Queue class
class QueueLL():
    # Initialize the queue
    def __init__(self):
        self.que = LinkedList() # Build from the linked list

    # add an item to the end of the queue
    def add(self, data):
        self.que.append(data) # use specific linked list function

    # remove the item in the front of the queue
    def dequeue(self):
        return self.que.rmvbeg() # use specific linked list function

    # display the structure as a string
    def __repr__(self):
        return str(self.que) # since the structure is a linked list, use the linked list __repr__() function

#Create an Array implementation of a Queue
class QueueA():
    def __init__(self):
        self.que = []

    def add(self, data):
        self.que.append(data)

    def dequeue(self):
        return self.que.pop(0)

    def __repr__(self):
        return str(self.que)

# Run the driver code
driver()
