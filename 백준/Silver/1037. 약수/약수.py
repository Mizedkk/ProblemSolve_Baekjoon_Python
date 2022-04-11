test_case = int(input())
cases = list(map(int, input().split()))

max = max(cases)
min = min(cases)
print(max * min)