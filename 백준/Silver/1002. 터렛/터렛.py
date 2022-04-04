# -1일 경우 x,y좌표와 반지름이 같을때
# 1일 경우 접할때 1. 바깥에서 2. 안에서
# 0일 경우 두점 사이의 거리가 바지름보다 길때

testcase = int(input())

for i in range(testcase):
  x1, y1, z1, x2, y2, z2 = map(int, input().split())
  ran = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
  if ran == 0 and z1 == z2:
    print(-1)
  elif z1 + z2 == ran or ran == abs(z2 - z1):
    print(1)
  elif abs(z1 - z2) < ran < z1 + z2:
    print(2)
  else:
    print(0)