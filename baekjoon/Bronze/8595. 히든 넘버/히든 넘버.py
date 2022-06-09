import sys

n = int(sys.stdin.readline())
st = sys.stdin.readline()
answer = ''

for i in st:
  if i in "0123456789":
    answer += i
  else:
    answer += ' '

answer = list(map(int, answer.split()))
print(sum(answer))