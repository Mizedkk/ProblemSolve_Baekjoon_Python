case = sorted(list(map(int, input().split())))

if case[0] == case[1] == case[2]:
  print("2")
elif (case[0] ** 2) + (case[1] ** 2) == case[2] ** 2:
  print("1")
else:
  print("0")
