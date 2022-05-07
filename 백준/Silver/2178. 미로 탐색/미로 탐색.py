import sys
from collections import deque


def main():
    n, m = map(int, sys.stdin.readline().split())
    case = []
    for _ in range(n):
        case.append(list(map(int, list(sys.stdin.readline().rstrip()))))

    def check_xy(y, x):
        return 0 <= y < n and 0 <= x < m

    def bfs():
        ck_case = [[False] * m for _ in range(n)]
        dx = (0, 0, 1, -1)
        dy = (1, -1, 0, 0)
        dq = deque()
        dq.append((0, 0, 1))
        while dq:
            y, x, cnt = dq.popleft()
            ncnt = cnt + 1

            if y == n - 1 and x == m - 1:
                return cnt

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if check_xy(ny, nx) and case[ny][nx] == 1 and not ck_case[ny][nx]:
                    ck_case[ny][nx] = True
                    dq.append((ny, nx, ncnt))
    print(bfs())


if __name__ == "__main__":
    main()