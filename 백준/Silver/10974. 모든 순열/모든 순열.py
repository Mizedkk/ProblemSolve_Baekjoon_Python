from itertools import permutations as pt


n = int(input())
case = [i for i in range(1, n + 1)]
case = list(pt(case))
for i in case:
  print(*i)
