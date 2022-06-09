for _ in range(3):
  sum = 0
  k = int(input())
  for i in range(k):
    sum += int(input())
  if sum == 0:
    print(0)
  elif sum > 0:
    print("+")
  else:
    print("-")
    