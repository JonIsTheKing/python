// rotate array n times
n = int(input('Please enter number'))
ik
arr = [1,2,3,4]

def rotateArray():
    temp = arr[0]
    for i in range(len(arr)-1):
      arr[i] = arr[i+1]
    arr[-1] = temp
    print(arr)

for i in range(n):
  rotateArray()
