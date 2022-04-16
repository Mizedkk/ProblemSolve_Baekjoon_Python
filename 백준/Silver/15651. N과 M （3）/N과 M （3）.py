from itertools import product

num, n = map(int, input().split())

case = [i for i in range(1, num + 1)]

k = list(product(case, repeat=n))

for i in k:

  print(*i)
  