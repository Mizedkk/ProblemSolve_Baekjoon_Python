from collections import Counter
import sys

for _ in range(3):
  case = list(map(int, sys.stdin.readline().split()))
  case_ct = Counter(case)
  if case_ct[1] == 1:
    print("C")
  elif case_ct[1] == 2:
    print("B")
  elif case_ct[1] == 3:
    print("A")
  elif case_ct[1] == 4:
    print("E")
  else:
    print("D")
