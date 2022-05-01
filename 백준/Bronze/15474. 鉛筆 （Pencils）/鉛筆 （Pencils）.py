N,A,B,C,D = map(int, input().split())

a = A
b = B
c = C
d = D
while N > A:
  A += a
  B += b

while N > C:
  C += c 
  D += d

print(min(B, D))
  