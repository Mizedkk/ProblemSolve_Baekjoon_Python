from itertools import permutations as pt

num, n = map(int, input().split())
case = list(map(int, input().split()))
case.sort()
case = pt(case, n)

for i in case:
  print(*i)
  