n,a = map(int, input().split())
n *= 1000
if 7000 * a <= n:
  print(7000 * a)
elif 3500 * a <= n:
  print(3500 * a)
elif 1750 * a <= n:
  print(1750 * a)
else:
  print(0)