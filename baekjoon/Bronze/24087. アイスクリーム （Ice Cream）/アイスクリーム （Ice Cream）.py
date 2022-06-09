s = int(input())
a = int(input())
b = int(input())

cnt = 0
while a + b * cnt < s:
  cnt += 1

print(250 + 100 * cnt)

