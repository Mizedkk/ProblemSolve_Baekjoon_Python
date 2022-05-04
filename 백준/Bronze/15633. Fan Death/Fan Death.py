n = int(input())

tp = 0
for i in range(1, n + 1):
  if n % i == 0:
    tp += i

print(tp*5 - 24)
