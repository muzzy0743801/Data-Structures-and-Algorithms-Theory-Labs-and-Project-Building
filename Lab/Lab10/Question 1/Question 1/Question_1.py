class CreateStack:
  def __init__(self, Capacity):
    self.Top = -1
    self.MAXSTK = Capacity
    self.List = ['' for i in range(self.MAXSTK)]
  def IsEmpyty(self):
    if self.Top == -1:
      return True
    return False
  def Push(self, item):
    if self.Top != self.MAXSTK-1:
      self.Top += 1
      self.List[self.Top] = item
    else:
      print("Stact is Full")
  def Pop(self):
    if(self.Top == -1):
      return '0'
    else:
      item = self.List[self.Top]
      self.List[self.Top] = ''
      self.Top -= 1
      return item
  def Peek(self):
    return self.List[self.Top]
def Polish(Q):
  stack = CreateStack(100)
  P = ""
  Q += ")"
  stack.Push("(")
  CounterQ = 0
  while(CounterQ <= len(Q)-1):
    item = Q[CounterQ]
    if(item != '+' and item != '-' and item != '*' and item != '/' and item != "%" and item != '^' and item != '(' and item != ')'):
      P += item
      CounterQ += 1
    elif(item == '('):
      stack.Push(item)
      CounterQ += 1
    elif(item == "+" or item == "-"):
      while(True):
        a = stack.Pop()
        if (a == '('):
          a = stack.Push(a)
          break
        else:
          P += a
      stack.Push(item)
      CounterQ += 1
    elif (item == "*" or item == "/" or item == "%"):
      while(True):
        a = stack.Pop()
        if(a == '('):
          stack.Push(a)
          break
        elif(item == "+" or item == "-"):
          stack.Push(a)
          break
        else:
          P += a
      stack.Push(item)
      CounterQ += 1
    elif(item == "^"):
      while(True):
        a = stack.Pop()
        if(a == '('):
          stack.Push(a)
          break
        elif(item != "^"):
            stack.Push(a)
            break
        else:
            P += a
      stack.Push(item)
      CounterQ += 1
    elif(item == ")"):
      while(True):
        a = stack.Pop()
        if(a == '0'):
          break
        if(a != '('):
            P += a
        else:
            break
      return P
print(Polish(input("Enter Equation: ")))