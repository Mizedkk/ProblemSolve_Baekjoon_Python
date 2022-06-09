for _ in range(3):
  a,b,c,d,e,f = map(int, input().split())
  s = f - c
  m = e - b
  h = d - a
  if s < 0:
    s = 60 + s
    m -= 1
  if m < 0:
    m = 60 + m
    h -= 1
  print(h, m, s)