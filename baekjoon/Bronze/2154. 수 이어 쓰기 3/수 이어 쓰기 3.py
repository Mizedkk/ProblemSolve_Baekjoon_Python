import sys


def main():
    iter_num = int(sys.stdin.readline())
    case_str = ""
    for num in range(1, iter_num + 1):
        case_str += str(num)
    print(case_str.find(str(iter_num)) + 1)


if __name__ == "__main__":
    main()