a,b,c = map(int, input().split())

if a == b == c:
  print("*")
else:
  if b == c and a != b:
    print("A")
  elif a == c and b != a:
    print("B")
  else:
    print("C")