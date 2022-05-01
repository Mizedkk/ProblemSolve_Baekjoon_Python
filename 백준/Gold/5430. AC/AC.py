from collections import deque
import sys
re = int(sys.stdin.readline())

# R ; 뒤집기
# D ; 버리기

for _ in range(re):
  cmd = sys.stdin.readline().rstrip()
  case_len = int(sys.stdin.readline())
  s = sys.stdin.readline().rstrip()[1:-1].split(",")
  dq = deque(s)
  if case_len == 0:
    dq = deque()
  cnt = 0

  for i in cmd:
    if i == "R":
      cnt += 1
    elif i == 'D':
      if len(dq) == 0:
          print('error')
          break
      else:
          if cnt % 2 == 0:
              dq.popleft()
          else:
              dq.pop()
  else:
    if cnt % 2 == 0:
      print("[" + ",".join(dq) + "]")
    else:
      dq.reverse()
      print("[" + ",".join(dq) + "]")