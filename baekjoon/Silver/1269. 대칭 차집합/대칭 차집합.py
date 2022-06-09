a, b = map(int, input().split())
case1 = set(map(int, input().split()))
case2 = set(map(int, input().split()))
print(len(case1 - case2) + len(case2 - case1))