n = int(input())
case = list(map(int, input().split()))

for i in range(1, min(case) + 1):
  j = 0
  for k in case:
    if k % i == 0:
      j += 1
    else:
      break
  if j == len(case):
    print(i)
  else:
    pass