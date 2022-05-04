a,b,c,d = map(int, input().split())
s = (((a*c)/b)/d) * 0.5
if int(s) == s:
  print(1)
else:
  print(0)