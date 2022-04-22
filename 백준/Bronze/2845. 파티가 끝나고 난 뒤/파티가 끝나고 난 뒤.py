a, b = map(int, input().split())
case = list(map(int, input().split()))
case = list(map(lambda x: x - a * b, case))
print(*case)