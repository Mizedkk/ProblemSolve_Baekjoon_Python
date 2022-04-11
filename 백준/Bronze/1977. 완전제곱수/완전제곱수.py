import math

a = int(input())
b = int(input())

case = []
total = 0

for i in range(a, b + 1):
  if int(math.sqrt(i)) == math.sqrt(i):
    case.append(i)

if len(case) == 0:
  print(-1)
else:
  print(sum(case))
  print(case[0])
