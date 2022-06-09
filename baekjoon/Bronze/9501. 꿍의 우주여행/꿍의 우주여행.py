import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, T = map(int, sys.stdin.readline().split())
        cnt = 0
        for _ in range(N):
            v, f, c = map(int, sys.stdin.readline().split())
            if T <= v * (f / c):
                cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()
