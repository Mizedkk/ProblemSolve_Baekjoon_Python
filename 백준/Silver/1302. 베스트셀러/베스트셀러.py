from collections import defaultdict
import sys


def main():
    case_dict = defaultdict(int)
    iter_num = int(sys.stdin.readline())
    for _ in range(iter_num):
        case = input()
        case_dict[case] += 1

    answer = sorted(zip(case_dict.keys(), case_dict.values()), key=lambda x: (-x[1], x[0]))
    print(answer[0][0])


if __name__ == "__main__":
    main()