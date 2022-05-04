from collections import Counter


a, b = map(int, input().split())
case = list(map(int, input().split()))
case = Counter(case).most_common()
answer = []
for a in case:
  answer.extend([a[0]] * a[1])
print(*answer)
  