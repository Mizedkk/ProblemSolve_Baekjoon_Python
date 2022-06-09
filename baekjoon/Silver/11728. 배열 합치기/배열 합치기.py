a, b = map(int, input().split())
case = list(map(int, input().split()))
case.extend(list(map(int, input().split())))
print(*sorted(case))
