case = list(map(int, input().split()))
count = 0
for i in case:
  if i > 0:
    count += 1
print(count)