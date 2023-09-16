from numpy import array

def sorter(array,starter):
  for i in range (len(array) - 1):
    checker = True
    for j in range (len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j + 1]
        array[j + 1] = array[j]
        array[j] = temp
        checker = False
    if checker == True:
      break


def binary(array,number):
    last = int(len(array))
    first = 0
    while(first <= last):
        mid = int((last + first) / 2)
        print(first,last,sep='\n')
        if (array[mid] == number):
          print("Found")
        elif (array[mid] > number):
          last = mid + 1
        else:
          first = mid -1

array = array([55,70,80,60,92,88])
sorter(array,0)
binary(array,55)
print(array)
