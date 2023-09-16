def Fib(Num):
	if Num == 0 or Num == 1:
		return Num
	return (Fib(Num-2)+Fib(Num-1))
for i in range(7):
	print(Fib(i),end = "")