from collections import Counter

n = int(input())
for i in range(n):
  str1, str2 = input().split()
  str1 = Counter(str1)
  str2 = Counter(str2)
  if str1 == str2:
    print("Possible")
  else:
    print("Impossible")