num = int(input())

for _ in range(num):
  a, b, c = map(int, input().split())

  if a + c > b:
    print("do not advertise")
  elif a + c == b:
    print("does not matter")
  else:
    print("advertise")