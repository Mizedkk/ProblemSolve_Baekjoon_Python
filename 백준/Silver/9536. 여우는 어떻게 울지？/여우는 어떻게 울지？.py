n = int(input())

for i in range(n):
  sound = list(input().split())
  while True:
    st = list(input().split())
    if st[0] == "what":
      break
    sound = list(filter(lambda x : x != st[2], sound))

  print(" ".join(sound))