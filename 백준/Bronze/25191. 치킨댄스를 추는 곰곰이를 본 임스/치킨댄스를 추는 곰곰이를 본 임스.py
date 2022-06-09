chicken = int(input())
cola, can = map(int, input().split())

if chicken - (cola//2 + can) > 0:
    print(cola//2 + can)
else:
    print(chicken)