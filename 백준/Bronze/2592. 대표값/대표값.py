import sys
from collections import Counter

def main():
    case = []
    for _ in range(10):
        case.append(int(sys.stdin.readline()))
    ct = Counter(case)

    print(sum(case)//10)
    print(ct.most_common(1)[0][0])


if __name__ == "__main__":
    main()