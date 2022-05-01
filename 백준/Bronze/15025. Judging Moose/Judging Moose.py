a, b = map(int, input().split())

if a == b != 0:
  print(f"Even {a+b}")
elif a == b == 0:
  print("Not a moose")
else:
  print(f"Odd {max(a,b) * 2}")