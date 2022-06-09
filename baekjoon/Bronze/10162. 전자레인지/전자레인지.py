time = int(input())

A = time // 300
time %= 300
B = time // 60
time %= 60
C = time // 10
time %= 10

if time != 0:
  print(-1)
else:
  print(f"{A} {B} {C}")  

