import sys


def main():
    T = int(input())
    for _ in range(T):
        N, C = map(int, input().split())
        cnt = 1
        temp = C
        while N > (C * cnt):
            cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()