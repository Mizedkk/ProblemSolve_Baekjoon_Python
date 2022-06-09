import sys


def main():
    iter_num = int(sys.stdin.readline())
    case = []
    for _ in range(iter_num):
        case.append(sys.stdin.readline())

    cp_case = sorted(case)
    rcp_case = sorted(case, reverse=True)
    if cp_case == case:
        print("INCREASING")
    elif rcp_case == case:
        print("DECREASING")
    else:
        print("NEITHER")


if __name__ == "__main__":
    main()
