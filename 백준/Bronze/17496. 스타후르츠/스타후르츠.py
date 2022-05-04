a, b, c, d = map(int, input().split())

sum = 0
for i in range(1, a + 1, b):
  if i == 1 : continue
  sum += c * d
print(sum)