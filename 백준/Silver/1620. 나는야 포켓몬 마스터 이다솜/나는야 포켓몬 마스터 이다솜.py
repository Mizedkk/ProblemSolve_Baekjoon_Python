pk = {}
a, b = map(int, input().split())
for i in range(1, a + 1):
  st = input()
  pk[st] = i
  pk[str(i)] = st

for i in range(b):
  st = input()
  print(pk[st])