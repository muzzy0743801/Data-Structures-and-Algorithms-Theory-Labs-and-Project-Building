# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OJG7GhXCnfQJdF2jjfgIVywbKHYkrU_h
"""

# node structure
class Node:
  #constructor to create a new node
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

#class Linked List
class LinkedList:
  #constructor to create an empty LinkedList
  def __init__(self):
    self.head = None

# test the code    
# create an empty LinkedList                 
MyList = LinkedList()

#Add first node.
first = Node(5)
#linking with head node
MyList.head = first

#Add second node.
second = Node(7)
#linking with first node
second.prev = first
first.next = second

#Add third node.
third = Node(3)
#linking with second node
third.prev = second
second.next = third

# node structure
class Node:
  #constructor to create a new node
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

#class Linked List
class LinkedList:
  #constructor to create an empty LinkedList
  def __init__(self):
    self.head = None

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

# test the code    
# create an empty LinkedList                 
MyList = LinkedList()

#Add first node.
first = Node(7)
#linking with head node
MyList.head = first

#Add second node.
second = Node(40)
#linking with first node
second.prev = first
first.next = second

#Add third node.
third = Node(6)
#linking with second node
third.prev = second
second.next = third

#print the content of list 
MyList.PrintList()



# node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the start of the list
  def push_front(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      self.head.prev = newNode
      newNode.next = self.head
      self.head = newNode

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

# test the code                  
MyList = LinkedList()

#Add three elements at the start of the list.
MyList.push_front(10)
MyList.PrintList()
MyList.push_front(20)
MyList.PrintList()
MyList.push_front(30)
MyList.PrintList()
MyList.push_front(100)
MyList.PrintList()
MyList.push_front(1000)
MyList.PrintList()

MyList.PrintList()

# node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode
      newNode.prev = temp

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

# test the code                  
MyList = LinkedList()

#Add three elements at the end of the list.
MyList.push_back(1000)
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.push_back(100)
MyList.PrintList()



MyList.push_back(1000)
MyList.push_back(100)
MyList.PrintList()

# node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode
      newNode.prev = temp

  #Inserts a new element at the given position
  def push_at(self, newElement, position):     
    newNode = Node(newElement)
    if(position < 1):
      print("\nposition should be >= 1.")
    elif (position == 1):
      newNode.next = self.head
      self.head.prev = newNode
      self.head = newNode
    else:    
      temp = self.head
      for i in range(1, position-1):
        if(temp != None):
          temp = temp.next   
      if(temp != None):
        newNode.next = temp.next
        newNode.prev = temp
        temp.next = newNode  
        if (newNode.next != None):
          newNode.next.prev = newNode
      else:
        print("\nThe previous node is null.")  

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

# test the code                  
MyList = LinkedList()

#Add three elements in the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.PrintList()

#Insert an element at position 2
MyList.push_at(100, 2)
MyList.PrintList() 

#Insert an element at position 1
MyList.push_at(200, 2)
MyList.PrintList()