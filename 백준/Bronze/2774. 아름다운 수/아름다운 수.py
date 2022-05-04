from collections import Counter

n = int(input())
for _ in range(n):
  s = input()
  s = Counter(s)
  print(len(s.keys()))