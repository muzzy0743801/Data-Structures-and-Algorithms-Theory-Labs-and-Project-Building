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
        while True:
            swapped = 0
            temp = self.start
            while(temp.next is not None):
                num0 = temp.data
                num1 = temp.next.data
                if(num0 > num1):
                    temp.data = num1
                    temp.next.data = num0
                    swapped = 1
                else:
                    temp = temp.next
            if swapped == 0:
                break
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
MyList.Insert(50)
MyList.Insert(30)
MyList.Insert(8)
MyList.Insert(65)
MyList.Insert(89)
MyList.Insert(85)
MyList.Insert(7)
print("Given List: ")
MyList.Print()
print("Your Sorted List is: ")
MyList.Sort()
MyList.Print()