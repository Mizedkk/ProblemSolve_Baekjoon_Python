n = int(input())
for _ in range(n):
  j = int(input())
  case = list(map(int, input().split()))
  print(min(case), max(case))