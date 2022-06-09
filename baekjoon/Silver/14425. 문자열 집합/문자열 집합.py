a, b = map(int, input().split())
case1 = set()
case2 = []
for i in range(a):
  case1.add(input())
for i in range(b):
  case2.append(input())

count = 0
for i in case2:
  if i in case1:
    count += 1

print(count)