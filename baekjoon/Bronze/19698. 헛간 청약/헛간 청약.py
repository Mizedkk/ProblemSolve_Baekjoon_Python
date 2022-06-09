N,W,H,L = map(int, input().split())

if N < (W//L) * (H//L):
  print(N)
else:
  print((W//L) * (H//L))
