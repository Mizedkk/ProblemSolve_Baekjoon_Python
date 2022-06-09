import sys
from itertools import combinations

case = []

for i in range(9):
  case.append(int(sys.stdin.readline()))

case = list(combinations(case, 7))
answer = []
for i in case:
  if sum(i) == 100:
    answer = list(i)
    break

answer.sort()

for i in answer:
  print(i)