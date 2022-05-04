a, b, c = map(int, input().split())
n = int(input())

h = n // 3600
n %= 3600
m = n // 60
n %= 60
s = n

c += s
if c >= 60:
  b += 1
  c %= 60
b += m
if b >= 60:
  a +=1
  b %= 60
a += h
if a >= 24:
  a %= 24

print(a, b, c)