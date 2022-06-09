a, b, c = map(int, input().split())
num = a * b - c
if num < 0:
  print(0)
else:
  print(a * b - c)