max = 0
a = 0
b = 0
for i in range(1, 10):
  case = list(map(int, input().split()))
  for j in range(len(case)):
    if max < case[j]:
      max = case[j]
      a = i
      b = j + 1

print(max)
print(a, b)
