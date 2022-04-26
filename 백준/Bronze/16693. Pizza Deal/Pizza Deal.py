import math

a, b = map(int, input().split())
c, d = map(int, input().split())

case1 = a / b
case2 = ((c ** 2) * math.pi) / d

if case1 > case2:
  print("Slice of pizza")
else:
  print("Whole pizza")