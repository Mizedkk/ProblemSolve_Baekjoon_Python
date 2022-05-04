from collections import Counter

str1 = Counter(input())
str2 = Counter(input())
str1.subtract(str2)
sum = 0
for i in str1.values():
  sum += abs(i)

print(sum)