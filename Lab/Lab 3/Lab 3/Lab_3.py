import numpy as np
arr = np.array([input("Enter Player Name: ") for i in range (int(input("How Many Player are there: ")))])
for x in range(len(arr)):
  print(arr[x],end="")
