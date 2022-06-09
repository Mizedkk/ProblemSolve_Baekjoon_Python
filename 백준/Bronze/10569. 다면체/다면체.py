iter_num = int(input())
for _ in range(iter_num):
    V, E = map(int, input().split())
    print(2 - V + E)