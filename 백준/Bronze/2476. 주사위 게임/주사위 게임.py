n = int(input())
max_num = 0
for _ in range(n):
  a,b,c = sorted(map(int, input().split()))
  answer = 0
  if a == b == c:
    answer = 10000 + a * 1000
    if max_num < answer : max_num = answer
  elif a == b:
    answer = 1000 + b * 100
    if max_num < answer : max_num = answer
  elif b == c:
    answer = 1000 + b * 100
    if max_num < answer : max_num = answer
  else:
    answer = max(a,b,c) * 100
    if max_num < answer : max_num = answer

print(max_num)