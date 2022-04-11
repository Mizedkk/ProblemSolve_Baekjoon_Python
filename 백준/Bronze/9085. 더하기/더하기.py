import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
  T = int(input())
  case = list(map(int, input().split()))
  print(sum(case))
