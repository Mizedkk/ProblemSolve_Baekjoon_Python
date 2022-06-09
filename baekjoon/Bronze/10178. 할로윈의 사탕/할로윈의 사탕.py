n = int(input())
for _ in range(n):
  a, b = map(int, input().split())
  a, b = divmod(a, b)
  print(f"You get {a} piece(s) and your dad gets {b} piece(s).")