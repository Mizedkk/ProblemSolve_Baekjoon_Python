n = int(input())
for i in range(1, n + 1):
  case =sorted(map(int, input().split()))
  print(f"Scenario #{i}:")
  if case[0] ** 2 + case[1] ** 2 == case[2] ** 2:
    print("yes")
  else:
    print("no")
  print("")