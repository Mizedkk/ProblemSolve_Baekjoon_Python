from itertools import combinations as cb

num, n = map(int, input().split())
case = list(map(int, input().split()))
case.sort()
case = cb(case, n)

for i in case:
  print(*i)
  