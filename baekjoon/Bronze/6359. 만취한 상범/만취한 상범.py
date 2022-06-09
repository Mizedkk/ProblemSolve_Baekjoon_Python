t = int(input())
for _ in range(t):
  n = int(input())
  case = [True * i for i in range(n + 1)]
  for i in range(2, n + 1):
    for j in range(i, len(case), i):
      if case[j]:
        case[j] = False
      else:
        case[j] = True
  case = case[1:]
  print(case.count(True))