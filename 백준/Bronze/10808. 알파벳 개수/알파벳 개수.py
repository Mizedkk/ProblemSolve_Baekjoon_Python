import string

case = list(string.ascii_lowercase)
str = input()
for i in range(len(case)):
  print(str.count(case[i]), end=" ")