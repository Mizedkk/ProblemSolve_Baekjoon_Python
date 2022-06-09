import sys

num = int(sys.stdin.readline())
case = []
for _ in range(num):
  case.append(int(sys.stdin.readline()))

case.sort(reverse=True)
for i in case:
  print(i)