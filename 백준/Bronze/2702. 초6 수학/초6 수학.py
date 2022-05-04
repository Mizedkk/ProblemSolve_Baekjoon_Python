import math

n = int(input())
for _ in range(n):
  a ,b = map(int, input().split())
  a, b = max(a, b), min(a, b)
  print((a*b)//math.gcd(a,b), math.gcd(a, b))