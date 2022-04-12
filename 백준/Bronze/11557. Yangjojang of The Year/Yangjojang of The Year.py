num = int(input())

for _ in range(num):
  num2 = int(input())
  case = []
  for i in range(num2):
    a, b = input().split()
    b = int(b)
    case.append([a, b])
  case.sort(key = lambda x : -x[1])
  print(case[0][0])