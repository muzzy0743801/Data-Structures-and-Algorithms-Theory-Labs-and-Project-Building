array = [int(input(f"Enter Element {i + 1}: ")) for i in range (int(input(f"Enter Number of Element: ")))]
def sort(i, j):
	if j < len(array-1):
		if array[j] > array [j + 1]:
			temp = array [j + 1]
			array [j + 1] = array[j]
			array[j] = temp
		else:
			sort(i,j+1)
	else:
		return True
for i in range(len(array) - 1):
	checker = True
	sort(i-1,0)
print(array)