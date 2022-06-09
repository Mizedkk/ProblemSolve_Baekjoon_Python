import sys


def main():
    iter_num = int(sys.stdin.readline())
    for _ in range(iter_num):
        num = int(sys.stdin.readline())
        cnt = 0
        for i in range(1, num + 1):
            if num % i == 0 :
                cnt += 1
        print(num, cnt)


if __name__ == "__main__":
    main()