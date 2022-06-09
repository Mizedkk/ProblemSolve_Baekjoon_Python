import sys
from collections import defaultdict
from collections import Counter


def main():
    num = int(sys.stdin.readline())
    case = list(map(int, sys.stdin.readline().split()))
    num2 = int(sys.stdin.readline())
    case2 = list(map(int, sys.stdin.readline().split()))
    ct = Counter(case)
    for i in case2:
        print(ct[i], end=" ")


if __name__ == "__main__":
    main()