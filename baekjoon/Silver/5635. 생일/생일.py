n = int(input())
case = []
for _ in range(n):
  name, d, m ,y = input().split()
  d = int(d)
  m = int(m)
  y = int(y)
  case.append([name, d, m, y])
case.sort(key = lambda x:(x[3], x[2], x[1]))
print(case[-1][0])
print(case[0][0])
