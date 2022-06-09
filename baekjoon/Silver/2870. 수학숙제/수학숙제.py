import sys

n = int(sys.stdin.readline())

answer = ''

for _ in range(n):
  st = sys.stdin.readline()
  for i in st:
    if i in "0123456789":
      answer += i
    else:
      answer += ' '
      
answer = list(map(int, answer.split()))
answer.sort()

for i in answer:
  print(i)