import sys
test_case, num = map(int, sys.stdin.readline().split())
case = []

for i in range(1, test_case + 1):
  if test_case % i == 0:
    case.append(i)
    
if num - 1 >= len(case):
  print(0)
else:
  print(case[num - 1])