n = int(input())

for _ in range(n):
  a, b = map(int, input().split())
  case1 = "No"
  case2 = "No"

  if 0 <= a <= 23 and 0 <= b <= 59:
    case1 = "Yes"

  if a in [1, 3, 5, 7, 8, 10, 12] and 1 <= b <= 31:
    case2 = "Yes"
  elif a in [4, 6, 9, 11] and 1 <= b <= 30:
    case2 = "Yes"
  elif a == 2 and 1 <= b <= 29:
    case2 = "Yes"

  print(case1, case2)