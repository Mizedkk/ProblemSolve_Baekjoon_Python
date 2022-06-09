n = int(input())
for _ in range(n):
  num = int(input())
  sum = 0
  for i in range(1, num + 1):
    sum += i * (((i + 1) * (i + 2))/2)
  print(int(sum))