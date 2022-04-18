a, b = map(int, input().split())

case1 = set()
case2 = set()

for i in range(a):
  st = input()
  case1.add(st)

for i in range(b):
  st = input()
  case2.add(st)

print(len(case1 & case2))
for i in sorted(list(case1 & case2)):
  print(i)
  