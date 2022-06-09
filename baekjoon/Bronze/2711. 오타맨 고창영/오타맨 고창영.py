num = int(input())
for _ in range(num):
  a, b = input().split()
  a = int(a)
  b = list(b)
  del b[a - 1]
  b = "".join(b)
  print(b)