n = int(input())
circle = 1
for _ in range(n):
  a, b = map(int, input().split())
  if circle == a:
    circle = b
  elif circle == b:
    circle = a

print(circle)