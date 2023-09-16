import time
class Sorting:
    def BucketSort(self,array):
        new_array = [array[i] for i in range(len(array))]
        new_array.sort()
        array = [new_array[i] for i in range(len(array))]
        return array
    def  BubbleSort(self,array):
        for i in range(len(array)):
            for j in range(len(array)):
                if array[i] < array[j]:
                    temp = array[j]
                    array[j] = array[i]
                    array[i] = temp
        return array
    def SelectionSort(self,array):
        index = 0
        for i in range(len(array)):
            index = i
            for j in range(i+1,len(array)):
                if array[j] < array[index]:
                    index = j
            if array[i] != array[index]:
                temp = array[i]
                array[i] = array[index]
                array[index] = temp
        return array
    def InsertionSort(self,array):
        for i in range(len(array)-1):
            if (array[i] > array[i + 1]):
                for j in range(i + 1,0,-1):
                    if (array[j - 1] > array[j]):
                        temp = array[j - 1]
                        array[j - 1] = array[j]
                        array[j] = temp
                    else:
                        break
        print(array)
        return array
    def Partition(self, array, low, high):
        i = (low-1)
        temp = array[high]
        for j in range(low, high):
            if array[j] <= temp:
                i = i+1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[high] = array[high], array[i+1]
        return (i+1)
    def QuickSort(self, array, low, high):
        if low < high:
            temp = self.Partition(array, low, high)
            self.QuickSort(array, low, temp-1)
            self.QuickSort(array, temp+1, high)
        return array
    def MergeSort(self,array):
        if len(array) > 1:
            mid = int(len(array)/2)
            L = array[:mid]
            R = array[mid:]
            self.MergeSort(L)
            self.MergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                array[k] = R[j]
                j += 1
                k += 1
        return array
class Searching:
    def BinarySearch(self,array,element):
        first = 0
        last = len(array) - 1
        while (last >= first):
            mid = int((first+last)/2)
            if(array[mid] == element):
                return mid
            elif(element > array[mid]):
                first = mid + 1
            else:
                last = mid -1
        return -1
    def LinerSearch(self,array,element):
        checker = 0
        for  i in range(len(array)):
            if(array[i]== element):
                return i
        return -1

if __name__ == '__main__':
    array = [input("Enter Element: ") for i in range(int(input("Enter Number of Element in array: ")))]
    timer = time.time()
    while True:
        type = input("Enter Operation\n1.Searching\n2.Sorting\nEnter Your Choice: ").lower()
        if(type == "searching" or type == "1"):
            search = Searching()
            element = input("Enter Element: ")
            while(True):
                type = input("Choice Algorithm\n1.Binary Search\n2.Liner Search\nEnter Your Choice: ").lower()
                if (type == "binary search" or type == "1"):
                    array.sort()
                    index = search.BinarySearch(array,element)
                    break
                elif(type == "linear search"or type == "2"):
                    index = search.LinerSearch(array,element)
                    break
                else:
                    print("Sorry Wrong Input: ")
            if index >= 0:
                print(f"{element} is on index {index+1} and Time Complexity of Algo is {time.time() - timer} secounds")
            else:
                print(f"Sorry {element} not Found and Time Complexity of Algo is {time.time() - timer} secounds")
            break
        elif(type == "sorting" or type == "2"):
            sorting = Sorting()
            while(True):
                type = input("Enter Algorithm\n1.Bucket Sort\n2.Bubble Sort\n3.Insertion Sort\n4.Merge Sort\n5.Quick Sort\n6.Selection Sort\nEnter Your Choice: ").lower()
                if (type == "bucket sort"or type == "1"):
                    print("Given array is:", array)
                    array = sorting.BucketSort(array)

                    break
                elif(type == "bubble sort"or type == "2"):
                    print("Given array is:", array)
                    array = sorting.BubbleSort(array)
                    print(timer)
                    break
                elif (type == "insertion sort"or type == "3"):
                    print("Given array is:", array)
                    array = sorting.InsertionSort(array)
                    break
                elif (type == "merge sort"or type == "4"):
                    print("Given array is:", array)
                    array = sorting.MergeSort(array)
                    break
                elif (type == "quick sort"or type == "5"):
                    print("Given array is:", array)
                    array = sorting.QuickSort(array,0,len(array)-1)
                    break
                elif (type == "selection sort"or type == "6"):
                    print("Given array is:", array)
                    array = sorting.SelectionSort(array)
                    break
                else:
                    print("Sorry Wrong Input: ")
            print(f"Sorted array is: {array} with Time Complexity of {time.time() - timer} secounds")
            break
        else:
            print("Sorry Wrong Input: ")