num = int(input())

case = []

for i in range(num):
    x, y = map(int, input().split())
    case.append([x, y])

for i in case:
  rank = 1
  for j in case:
    if i[0] < j[0] and i[1] < j[1]:
      rank += 1
  print(rank, end=" ")