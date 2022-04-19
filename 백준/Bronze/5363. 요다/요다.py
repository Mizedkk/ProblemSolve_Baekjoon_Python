n = int(input())
for i in range(n):
  s = list(input().split())
  print(" ".join(s[2:]) +" "+ " ".join(s[:2]))