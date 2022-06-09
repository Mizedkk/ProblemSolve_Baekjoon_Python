a, b = map(int, input().split())
case = list(map(int, input().split()))
case.sort()
print(case[b - 1])