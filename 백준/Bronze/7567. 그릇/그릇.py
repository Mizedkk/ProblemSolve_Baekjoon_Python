str = input()
char = ''
sum = 0

for i in range(len(str)):
  if str[i] == char:
    sum += 5
  else:
    char = str[i]
    sum += 10

print(sum)