from itertools import combinations_with_replacement as cwr
num, n = map(int, input().split())
case = list(map(int, input().split()))
case.sort()
case = cwr(case, n)

for i in case:
  print(*i)