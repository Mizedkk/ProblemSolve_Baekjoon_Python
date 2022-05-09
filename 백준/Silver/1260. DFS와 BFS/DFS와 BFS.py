import sys
from collections import deque


def main():

    n, m, v = map(int, sys.stdin.readline().split())
    case = [[0] * (n + 1) for _ in range(n + 1)]
    case_ck1 = [0] * (n + 1)
    case_ck2 = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        case[a][b] = case[b][a] = 1

    def dfs(v):
        case_ck1[v] = 1
        print(v, end=" ")
        for i in range(1, n + 1):
            if not case_ck1[i] and case[v][i]:
                dfs(i)

    def bfs(v):
        dq = deque()
        case_ck2[v] = 1
        dq.append(v)
        while dq:
            v = dq.popleft()
            print(v, end=" ")
            for i in range(1, n + 1):
                if not case_ck2[i] and case[v][i]:
                    dq.append(i)
                    case_ck2[i] = 1

    dfs(v)
    print("")
    bfs(v)


if __name__ == "__main__":
    main()