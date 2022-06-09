import sys


def main():
    num = int(sys.stdin.readline())
    case = list(map(int, sys.stdin.readline().split()))
    num2 = int(sys.stdin.readline())
    case2 = list(map(int, sys.stdin.readline().split()))
    case3 = set(case) & set(case2)
    answer = []
    for i in case2:
        if i in case3:
            answer.append(1)
        else:
            answer.append(0)
    print(*answer)


if __name__ == "__main__":
    main()
