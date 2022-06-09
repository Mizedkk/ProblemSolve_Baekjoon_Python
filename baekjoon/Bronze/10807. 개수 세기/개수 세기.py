from collections import Counter

num = int(input())
case = list(map(int, input().split()))
case = Counter(case)
answer = int(input())
print(case[answer])