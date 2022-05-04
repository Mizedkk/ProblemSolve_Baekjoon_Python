import sys

stack = []
answer = 0

st = sys.stdin.readline().rstrip()
for i in range(len(st)):
  if st[i] == "(":
    stack.append("(")
  else:
    if st[i - 1] == "(":
      stack.pop()
      answer += len(stack)
    else:
      stack.pop()
      answer += 1

print(answer)