import sys

test_case = int(sys.stdin.readline())

case = []
for i in range(test_case):
  a, b = map(int, sys.stdin.readline().split())
  case.append([a, b])

case.sort(key = lambda x :(x[1], x[0]))
for i in case:
  print(i[0],i[1])