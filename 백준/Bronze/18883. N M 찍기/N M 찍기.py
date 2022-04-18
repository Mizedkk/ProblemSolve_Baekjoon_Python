a, b = map(int, input().split())
case = [i for i in range(1, a * b + 1)]
for i in case:
  if i % b == 0:
    print(i)
  else:
    print(i, end=" ")