import math
import sys

def prime(num):
  answer = [False] * 2 + [True for i in range(num - 1)]
  for i in range(2, int(math.sqrt(num) + 1)):
    if answer[i]:
      for j in range(2*i, num + 1, i):
        answer[j] = False
  case = []
  for i in range(len(answer)):
    if answer[i]:
      case.append(i)
  return case


iter = int(sys.stdin.readline())
case = prime(10001)

for i in range(iter):
  test_num = int(input())
  for j in range(test_num // 2, 1, -1):
    if test_num - j in case and j in case:
      print(j ,test_num - j)
      break
  