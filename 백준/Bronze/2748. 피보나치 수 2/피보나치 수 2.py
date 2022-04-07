import sys

num = int(sys.stdin.readline())

case = [0 ,0]
dp = [0] * 100
dp[1] = 1
dp[2] = 1
for i in range(3, 100):
  dp[i] = dp[i - 1] + dp[i - 2]

print(dp[num])