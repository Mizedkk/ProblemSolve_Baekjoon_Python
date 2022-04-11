num = int(input())
case = list(map(int, input().split()))

total = 0
num = 1
for i in case:
  if i == 1:
    total += num
    num += 1
  else:
    num = 1

print(total)