n = int(input())
st = input()
count = 0
for i in st:
  if i in "aeiou":
    count += 1
print(count)