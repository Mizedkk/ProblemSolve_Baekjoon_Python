a,b,c = map(int, input().split())

ax,bx,cx = map(int, input().split())

if ax >= a and bx >= b and cx >= c:
  print("A")
elif ax >= a/2 and bx >= b and cx >= c:
  print("B")
elif bx >= b and cx >= c:
  print("C")
elif bx >= b/2 and cx >= c:
  print("D")
else:
  print("E")