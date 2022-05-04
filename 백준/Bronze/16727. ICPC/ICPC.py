Persepolis = 0
Esteghlal = 0

a, b = map(int, input().split())
Persepolis += a
Esteghlal += b

c, d = map(int, input().split())
Persepolis += d
Esteghlal += c

if Esteghlal > Persepolis:
  print("Esteghlal")
elif Esteghlal < Persepolis:
  print("Persepolis")
else:
  if d > b:
    print("Persepolis")
  elif d < b:
    print("Esteghlal")
  else:
    print("Penalty")