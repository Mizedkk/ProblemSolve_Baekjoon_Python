W = 0
for _ in range(6):
  a = input()
  if a == "W":
    W += 1

if 5 <= W <= 6:
  print(1)
elif 3 <= W <=4:
  print(2)
elif 1 <= W <= 2:
  print(3)
else:
  print(-1)