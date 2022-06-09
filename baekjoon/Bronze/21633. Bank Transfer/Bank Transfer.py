n = int(input())
if 25 + n * 0.01 <= 100:
  print(100)
elif 25 + n * 0.01 >= 2000:
  print(2000)
else:
  print(25 + n * 0.01)