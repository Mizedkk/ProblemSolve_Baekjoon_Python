case = []
n = int(input())
for i in range(n):
  name, k, m, e = input().split()
  k = int(k)
  m = int(m)
  e = int(e)
  case.append([name, k, m, e])

case.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))
for i in case:
  print(i[0])