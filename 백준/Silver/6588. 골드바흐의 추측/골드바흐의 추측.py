from math import sqrt
import sys

MAX = 1000000

dp = [False, False] +  [True] * (MAX - 1)
for i in range(2, int(sqrt(len(dp))) + 1):
  if dp[i]:
    for j in range(i * 2, len(dp), i):
      dp[j] = False

dp[2] = False

while True:
  num = int(sys.stdin.readline())
  if num == 0 : break
  for i in range(3, num + 1, 2):
    if dp[i] == True and dp[num - i] == True:
      print(f"{num} = {i} + {num - i}")
      break
  else:
    print("Goldbach's conjecture is wrong.")