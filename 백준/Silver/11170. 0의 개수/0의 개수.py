n = int(input())
for _ in range(n):
  a, b = map(int, input().split())
  case = [str(i) for i in range(a, b + 1)]
  count = 0
  for i in case:
    if "0" in i:
      count += i.count("0")
  print(count)