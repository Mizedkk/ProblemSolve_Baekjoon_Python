n = int(input())
for _ in range(n):
  case = sorted(map(int, input().split()))
  print(case[-3])