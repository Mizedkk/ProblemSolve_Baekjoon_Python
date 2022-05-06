import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    case = list(map(int, sys.stdin.readline().split()))
    case.sort()
    case_num = case[0] - 0.5 + k
    cnt = 1
    for i in case[1:]:
        if i < case_num:
            continue
        else:
            case_num = i - 0.5 + k
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()