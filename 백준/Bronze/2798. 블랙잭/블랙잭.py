from itertools import combinations
import sys

a, b = map(int, sys.stdin.readline().split())
case = map(int, sys.stdin.readline().split())
case = list(map(sum, combinations(case, 3)))

while True:
  if b in case:
    print(b)
    break
  else:
    b -= 1