num = int(input())
case = sorted(list(set(map(int, input().split()))))
print(*case)
