word = [[] for i in range(15)]

for _ in range(5):
  st = input()
  for i in range(len(st)):
    word[i].append(st[i])

answer = ''
for i in word:
  answer += ''.join(i)

print(answer)