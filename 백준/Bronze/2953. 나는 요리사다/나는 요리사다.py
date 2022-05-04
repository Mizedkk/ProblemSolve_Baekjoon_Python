case = []
for i in range(5):
  num = list(map(int, input().split()))
  case.append(sum(num))

print(case.index(max(case)) + 1, max(case))