// print numbers using recursion - head

def printNumbers(num):
  if num == 0:
    return
  
  print(num)
  printNumbers(num-1)

printNumbers(5)
