import heapq
import sys

n = int(sys.stdin.readline().rstrip())
case = []

for _ in range(n):
  c = int(sys.stdin.readline().rstrip())
  if c != 0:
    heapq.heappush(case, -c)
  else:
    try:
      print(-heapq.heappop(case))
    except:
      print(0)