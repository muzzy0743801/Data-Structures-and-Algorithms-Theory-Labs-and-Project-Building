def reverse(length,name):
    if(length >= 0):
        print(name[length],end="")
        length -= 1
        reverse(length,name)
    else:
        return
name = input("Enter Your Name: ")
print("The Name in reverse order will be: ",end="")
reverse(len(name)-1,name)
print()