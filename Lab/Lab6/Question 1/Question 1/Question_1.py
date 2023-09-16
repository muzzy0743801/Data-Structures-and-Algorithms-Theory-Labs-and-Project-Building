class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.start = None
    def Insert(self, value):
        newNode = Node(value)
        if(self.start == None):
            self.start = newNode
            return
        else:
            temp = self.start
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
    def Delete(self):
        nodeToDelete = self.start
        self.start = self.start.next
        nodeToDelete = None
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
MyList = LinkedList()
MyList.Insert(10)
MyList.Insert(20)
MyList.Insert(30)
print("Given List: ")
MyList.Print()
print("First Time Deletion: ")
MyList.Delete()
MyList.Print()
print("Second Time Deletion: ")
MyList.Delete()
MyList.Print()
print("Third Time Deletion: ")
MyList.Delete()
MyList.Print()