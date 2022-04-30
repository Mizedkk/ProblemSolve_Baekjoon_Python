n = int(input())
for _ in range(n):
  st1 = input()
  st2 = st1[::-1]
  st3 = int(st1) + int(st2)
  st3 = str(st3)
  if st3 == st3[::-1]:
    print("YES")
  else:
    print("NO")