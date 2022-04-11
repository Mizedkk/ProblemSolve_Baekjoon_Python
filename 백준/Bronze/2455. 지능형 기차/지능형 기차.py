case = []
for _ in range(4):
  case.append(list(map(int, input().split())))

total = 0
max = 0
for i in case:
  total -= i[0]
  total += i[1]
  if max < total:
    max = total
print(max)