from itertools import product as pd

num, n = map(int, input().split())
case = list(map(int, input().split()))
case.sort()
case = pd(case, repeat=n)

for i in case:
  print(*i)