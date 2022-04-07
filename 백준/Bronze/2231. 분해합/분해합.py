import sys

n = int(sys.stdin.readline())
answer = 0
for i in range(n + 1):
  a = list(map(int, str(i)))
  b = i + sum(a)
  if n == b:
    answer = i
    break
print(answer)