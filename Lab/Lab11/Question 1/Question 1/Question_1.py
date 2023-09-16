class queue:
    def __init__(self,length):
        self.array = [0 for i in range(length)]
        self.head = 0
        self.hail = -1
        self.sum1 = 0
        self.sum2 = 0
        return
    def Enqueue(self,element):
        if self.hail == len(self.array) -1:
            print("Your Queue is full after Enqueuing ")
            self.Print()
        else:
            self.hail +=1
            self.array[self.hail] = element
        return
    def Dequeue(self):
        if self.head > self.hail:
            print("Queue is Empty. Enter element first.")
            char = (input("Press Y or y to enter Element: ")).lower()
            if char == 'y':
                self.Enqueue(int(input("Enter Element: ")))
        else:
            temp = self.array[self.head]
            for i in range(len(self.array)-1):
                self.array[i] = self.array[i+1]
            self.array[len(self.array)-1] = ""
            return temp
    def Print(self):
        for i in range(len(self.array)):
            print(f"{i+1}.",self.array[i],end ="\t")
    def sum(self,element,i):
        if(i <= len(self.array)/2):
            self.sum1 += element
        elif(i < len(self.array)):
            self.sum2 += element
        else:
            self.sum2 += element
            print("\nSum of First Half of Array is",self.sum1)
            print("Sum of Secound Half of Array is",self.sum2)
number_of_Element = int(input("Enter Number of Element: "))
queue = queue(number_of_Element)
for i in range(1,number_of_Element+1):
    queue.Enqueue(i)
queue.Print()
for i in range(1,number_of_Element+1):
    element = queue.Dequeue()
    queue.sum(element,i)
print()