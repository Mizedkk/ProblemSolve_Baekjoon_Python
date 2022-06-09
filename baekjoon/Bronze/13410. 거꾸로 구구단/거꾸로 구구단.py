a, b = map(int, input().split())
case = []
for i in range(1, b + 1):
  case.append(int(str(a * i)[::-1]))

print(max(case))