s = input()
answer = set()

for i in range(len(s)):
  for j in range(len(s)):
    answer.add(s[i:j + 1])
print(len(answer) - 1)