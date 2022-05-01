a,b,c = map(int, input().split())

if c - 11 < 0:
  b -= 1
  c = 60 + c - 11
else:
  c -= 11

if b - 11 < 0:
  a -= 1
  b = 24 + b - 11
else:
  b -= 11

if a - 11 < 0:
  print(-1)
else:
  a -= 11
  print(1440 * a + 60 * b + c)