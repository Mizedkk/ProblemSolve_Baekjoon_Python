sc = []
so = []
for _ in range(4):
  sc.append(int(input()))
for _ in range(2):
  so.append(int(input()))
print(sum(sorted(sc, reverse=True)[:3]) + sorted(so, reverse=True)[0])