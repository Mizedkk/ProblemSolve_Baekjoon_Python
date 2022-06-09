case1 = list(map(int, input().split(":")))
case2 = list(map(int, input().split(":")))

if case2[2] - case1[2] < 0:
  case2[1] -= 1
  case2[2] = 60 + case2[2] - case1[2]
else:
  case2[2] -= case1[2]

if case2[1] - case1[1] < 0:
  case2[0] -= 1
  case2[1] = 60 + case2[1] - case1[1]
else:
  case2[1] -= case1[1]

if case2[0] - case1[0] < 0:
  case2[0] = 24 + case2[0] - case1[0]
else:
  case2[0] -= case1[0]

print(case2[0] * 3600 + case2[1] * 60 + case2[2])