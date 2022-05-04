n = int(input())
case = list(map(int, input().split()))
sum = 0
for i in case:
  for j in case:
    sum += abs(i - j)

print(sum)