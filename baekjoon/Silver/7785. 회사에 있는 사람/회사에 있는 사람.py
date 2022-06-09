num = int(input())
room = []
for i in range(num):
  a, b = input().split()
  if b == "enter":
    room.append(a)
  else:
    room.remove(a)

room.sort(reverse=True)
for i in room:
  print(i)