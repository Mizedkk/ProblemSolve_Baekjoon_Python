n = int(input())
result = []

for _ in range(n):
  case = []
  p = int(input())
  for _ in range(p):
    a, b = input().split()
    a = int(a)
    case.append([a, b])
  case.sort(key=lambda x : -x[0])
  result.append([case[0][0], case[0][1]])

for i in result:
  print(i[1])