class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
    def Insert(self, Value):
        newNode = Node(Value)
        if(self.start == None):
            self.start = newNode
            return
        else:
            temp = self.start
            while(temp.next is not None):
                temp = temp.next
            temp.next = newNode
    def Sort(self):
        temp = self.start
        while(temp.next is not None):
            num0 = temp.data
            num1 = temp.next.data
            if(num0 == num1):
                nodeToDelete = temp.next
                temp.next = temp.next.next
                nodeToDelete = None
            else:
                temp = temp.next
    def Print(self):
        temp = self.start
        i = 1
        if(temp is not None):
            while (temp is not None):
                print(f"{i}.",temp.data, end = " \t")
                i = i + 1
                temp = temp.next
        print()
        print()
MyList = LinkedList()
MyList.Insert(1)
MyList.Insert(2)
MyList.Insert(2)
MyList.Insert(3)
MyList.Insert(3)
MyList.Insert(3)
MyList.Insert(3)
print("Given List: ")
MyList.Print()
print("Your Sorted List is: ")
MyList.Sort()
MyList.Print()