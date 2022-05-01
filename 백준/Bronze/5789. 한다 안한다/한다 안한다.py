n = int(input())
for _ in range(n):
  st = input()
  print("Do-it" if st[len(st)//2] == st[len(st)//2 - 1] else "Do-it-Not")