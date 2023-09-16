def Print(Table,Start):
	if(Start <=9):
		print(f"{Table} x {Start} =",Table*Start)
		Print(Table,Start+2)
Print(2,1)