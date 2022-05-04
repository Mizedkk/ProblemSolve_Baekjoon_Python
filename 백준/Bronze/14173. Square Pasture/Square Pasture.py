wd = []
ht = []
for i in range(2):
  case = list(map(int,input().split()))
  wd.append(case[0])
  wd.append(case[2])
  ht.append(case[1])
  ht.append(case[3])

print(max((max(wd) - min(wd)), (max(ht) - min(ht))) ** 2)
  