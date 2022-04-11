num = int(input())
case = list(map(int, input().split()))
count = 0 
for i in case:
  if num == i:
    count += 1
print(count)