from numpy import array

def BinarySearch(array, number,first,last):
	index = -1
	while(first <= last):
		mid = int((first + last) / 2)
		if (array[mid] == number):
			Index = mid
			break
		elif (number > array[mid]):
			first = mid + 1
		elif (number < array[mid]):
			mid = first - 1
	return index
array = array([i for i in range (1,1001)])
print(BinarySearch(array, int(input("Enter Number: ")),0,len(array)-1))
input("Enter Number: ")
