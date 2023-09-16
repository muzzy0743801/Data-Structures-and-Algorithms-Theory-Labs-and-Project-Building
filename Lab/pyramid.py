
#Question 7
value = int(input("Enter Digit To calculate Factorial: "))
result = 1
for x in range(1,value):
	value = value * x
print(value)

"""
# Question 8
value = int(input("Enter ending value : "))
num0 = 0
num1 = 1
sum = 0
print(num0, num1, sep = "\t",end = "\t")
for x in range(value):
	sum = num0 + num1
	print(sum, end = "\t")
	num0 = num1
	num1 = sum


# Question 9
for x in range(8):
	for y in range(1,x+1):
		print(y,end="")
	for z in range(7,x,-1):
		print("*",end="")
	print()
print()


# Question 10
for x in range(5):
	for y in range(5):
		print("*",sep="",end="")
	print()
#input()
"""