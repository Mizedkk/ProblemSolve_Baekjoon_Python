from collections import Counter

n = int(input())
case = []
for i in range(n):
  case.append(input())

top = sorted(list(Counter(case).most_common()), key = lambda x: (-x[1], x[0]))
print(top[0][0])

