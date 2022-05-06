import sys


def main():
    n = int(input())
    data = list(map(int, sys.stdin.readline().split()))
    for i in range(1, n):
        data[i] = max(data[i], data[i] + data[i - 1])

    print(max(data))


if __name__ == "__main__":
    main()
