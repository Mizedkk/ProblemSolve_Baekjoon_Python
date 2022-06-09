num = int(input())
for i in range(1, num + 1):
  st = list(input().split())
  st = ' '.join(st[::-1])
  print(f"Case #{i}: {st}")