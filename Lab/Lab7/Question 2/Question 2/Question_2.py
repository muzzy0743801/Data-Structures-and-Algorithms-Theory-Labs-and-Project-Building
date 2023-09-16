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
  def PrintList(self, course):
    temp = self.head
    if(temp != None):
      while (temp != None):
        if(temp.data == course):
          print("Your Course is:",temp.data)
          print("Your Course's Prerequisites is: ",end="")
          while(temp != None):
            temp = temp.prev
            if (temp != None):
                if(temp.data != "PF"):
                    print(f"{temp.data}",end=" | ")
                else:
                    print(f"{temp.data}",end="")
        else:
            temp = temp.next
      print()
    else:
      print("The list is empty.")

# test the code    
# create an empty LinkedList                 
MyList = LinkedList()

#Add first node.
first = Node("PF")
#linking with head node
MyList.head = first

#Add second node.
second = Node("OOP")
#linking with first node
second.prev = first
first.next = second

#Add third node.
third = Node("DST")
#linking with second node
third.prev = second
second.next = third

fourth = Node("DBMS")
#linking with first node
fourth.prev = third
third.next = fourth

#Add third node.
fifth = Node("OOAD")
#linking with second node
fifth.prev = fourth
fourth.next = fifth

sixth = Node("AI")
#linking with second node
sixth.prev = fifth
fifth.next = sixth

seventh = Node("DP")
#linking with second node
seventh.prev = seventh
sixth.next = seventh
#print the content of list 
MyList.PrintList(input("Enter Course You Want To Check: "))
