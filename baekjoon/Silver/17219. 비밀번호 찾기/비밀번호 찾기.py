pk = {}
a, b = map(int, input().split())
for i in range(1, a + 1):
  id, pw = input().split()
  pk[id] = pw

for i in range(b):
  st = input()
  print(pk[st])