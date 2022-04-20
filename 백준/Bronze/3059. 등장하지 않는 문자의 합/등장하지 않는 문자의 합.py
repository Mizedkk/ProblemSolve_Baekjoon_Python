import sys
import string

asc_case = {}
A_Z = sum(range(65, 91))

for a, b in zip(string.ascii_uppercase, range(65, 91)):
  asc_case[a] = b

n = int(sys.stdin.readline())

for _ in range(n):
  st = sys.stdin.readline()
  
  case_sum = A_Z
  case_dict = asc_case.copy()
  
  for i in st:
    if i in case_dict:
      case_sum -= case_dict[i]
      case_dict[i] = 0
  print(case_sum)