n = int(input())
for _ in range(n):
  case = input().split()
  answer = float(case[0])
  for i in case[1:]:
    if i == "@":
      answer *= 3
    elif i == "%":
      answer += 5
    elif i == "#":
      answer -= 7

  print(f"{answer:.2f}")