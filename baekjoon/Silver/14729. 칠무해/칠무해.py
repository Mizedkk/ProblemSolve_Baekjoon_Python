n = int(input())
case = []
for _ in range(n):
  case.append(float(input()))

for i in sorted(case)[:7]:
  print(f"{i:.3f}")