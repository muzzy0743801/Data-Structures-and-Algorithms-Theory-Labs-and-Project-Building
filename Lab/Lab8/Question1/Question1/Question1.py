class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.start = None
    def Push(self, value):
        newNode = Node(value)
        if(self.start == None):
            self.start = newNode
            return
        else:
            temp = self.start
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
    def Print(self):
        temp = self.start
        i = 1
        if(temp != None):
            while (temp != None):
                print(f"{i}.",temp.data, end = " \t")
                i = i + 1
                temp = temp.next
        else:
            print("The list is now empty.")
        print()
        print()
    def Pop(self):
        temp0 = self.start
        temp1 = temp0.next
        if(temp0 != None):
            while (temp1.next != None):
                temp0 = temp0.next
                if(temp0.data == self.start):
                    break
                temp1 = temp0.next

            temp0.next = None
            print("Your Poped Item is:",temp1.data)
            temp1.next = None
MyList = LinkedList()
MyList.Push(10)
MyList.Push(20)
MyList.Push(30)
MyList.Pop()
MyList.Pop()
