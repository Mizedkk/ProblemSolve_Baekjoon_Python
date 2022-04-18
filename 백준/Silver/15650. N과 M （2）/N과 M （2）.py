from itertools import combinations

num, n = map(int, input().split())

case = [i for i in range(1, num + 1)]

k = list(combinations(case, n))

for i in k:

  print(*i)
  