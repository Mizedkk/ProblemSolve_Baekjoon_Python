a,b,c = sorted(map(int, input().split()))

if a == b:
  print("S")
elif b == c:
  print("S")
elif a + b == c:
  print("S")
else:
  print("N")