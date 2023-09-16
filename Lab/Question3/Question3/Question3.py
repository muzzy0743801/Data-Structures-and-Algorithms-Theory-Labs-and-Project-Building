length = int(input(f"Enter Number of Element: "))
array = [int(input(f"Enter Element {i + 1}: ")) for i in range (length)]
def caller(i,length):
	if(i < length):
		checker = True
		checker = sort(i,0, checker)
		if checker == True:
			return
		else:
			 caller(i+1,length)
	else:
		return
	
def sort(i, j, checker):
	if j < length - i - 1:
		if array[j] > array [j + 1]:
			temp = array [j + 1]
			array [j + 1] = array[j]
			array[j] = temp
			checker = False
		sort(i,j+1,checker)
	else:
		return checker
caller(0,length-1)
print(array)