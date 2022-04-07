import sys

test_case = int(sys.stdin.readline())

case = []
for i in range(test_case):
  str = input()
  case.append(str)

case = list(set(case))
case.sort(key = lambda x :(len(x), x))
for i in case:
  print(i)