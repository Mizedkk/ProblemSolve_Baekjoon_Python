from collections import deque
import sys

dq = deque()
dq2 = deque()
num = int(sys.stdin.readline())
dq.extend([i for i in range(1, num + 1)])

while len(dq) != 1:
  dq.popleft()
  num = dq.popleft()
  dq.append(num)

print(dq[0])