case = list(map(int ,input().split()))
odd_case = []
answer = 1
for i in case:
  if i % 2 != 0:
    odd_case.append(i)

if len(odd_case) == 0:
  for i in case:
    answer *= i
  print(answer)
else:
  for i in odd_case:
    answer *= i
  print(answer)
