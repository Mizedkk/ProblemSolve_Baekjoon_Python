n = int(input())
for _ in range(n):
  a, b = map(int, input().split())
  try:
    b8 = int(str(b), 8)
  except:
    b8 = 0
  try:
    b16 = int(str(b), 16)
  except:
    b16 = 0
  print(f"{a} {b8} {b} {b16}")
