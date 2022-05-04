case = list(input().split())
for i in range(len(case)):
  case[i] = case[i].replace('5', '6')
max = eval(f"{case[0]} + {case[1]}")
for i in range(len(case)):
  case[i] = case[i].replace('6', '5')
min = eval(f"{case[0]} + {case[1]}")
print(min, max)