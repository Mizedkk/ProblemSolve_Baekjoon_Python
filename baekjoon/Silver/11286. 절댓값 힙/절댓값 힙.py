import heapq
import sys


def main():
    hq = []
    iter_num = int(sys.stdin.readline())
    for _ in range(iter_num):
        case_num = int(sys.stdin.readline())
        if case_num:
            heapq.heappush(hq, (abs(case_num), case_num))
        else:
            if hq:
                print(heapq.heappop(hq)[1])
            else:
                print(0)


if __name__ == "__main__":
    main()