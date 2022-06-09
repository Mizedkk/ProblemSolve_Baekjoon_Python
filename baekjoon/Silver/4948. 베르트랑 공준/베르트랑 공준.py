import math

def prime(num):
  if num==1:
    print(1)
    return
  
  array = [True for i in range(2*num + 1)]
  array[0] = False
  array[1] = False
  
  for i in range(int(math.sqrt(2 * num)) + 1):
    if array[i]:
      for j in range(2 * i, 2* num + 1, i):
        array[j] = False

  count = 0
  
  for i in range(num + 1, 2 * num + 1):
    if array[i]:
      count += 1

  print(count)
  
while True:
  num = int(input())
  if num == 0 : break
  prime(num)

