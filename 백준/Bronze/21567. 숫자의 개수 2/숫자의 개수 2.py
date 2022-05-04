from collections import Counter
a = int(input())
b = int(input())
c = int(input())
total = str(a*b*c)
total = Counter(total)

for i in range(10):
  print(total[str(i)])