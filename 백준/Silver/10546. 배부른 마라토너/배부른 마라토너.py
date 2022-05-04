n = int(input())
case = {}

for i in range(n):
  st = input()
  if st in case.keys():
    case[st] += 1
  else:
    case[st] = 1

for i in range(n - 1):
  st = input()
  if st in case.keys():
    case[st] -= 1


for key, value in case.items():
  if value == 1:
    print(key)