a, b = map(int, input().split())
b, a = max(a, b), min(a, b)
if b - a <= 1:
  print(0)  
else:
  print(b - a - 1)
print(*[i for i in range(a + 1, b)])