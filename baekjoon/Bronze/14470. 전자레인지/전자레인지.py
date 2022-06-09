case = []
for _ in range(5):
  case.append(int(input()))

count = 0
flag = 0

while case[0] != case[1]:
  if case[0] < 0:
    case[0] += 1
    count += case[2]
  elif case[0] == 0 and flag == 0:
    count += case[3]
    flag = 1
  else:
    case[0] += 1
    count += case[4]


print(count)