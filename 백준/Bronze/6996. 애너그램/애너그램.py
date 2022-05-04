from collections import Counter

n = int(input())
for i in range(n):
  str1, str2 = input().split()
  C1 = Counter(str1)
  C2 = Counter(str2)
  if C1 == C2:
    print(f"{str1} & {str2} are anagrams.")
  else:
    print(f"{str1} & {str2} are NOT anagrams.")