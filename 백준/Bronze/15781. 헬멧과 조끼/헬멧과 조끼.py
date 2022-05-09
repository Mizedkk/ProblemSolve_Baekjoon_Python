import sys


def main():
  a, b = map(int, input().split())
  case1 = list(map(int, input().split()))
  case2 = list(map(int, input().split()))
  print(max(case1) + max(case2))


if __name__ == "__main__":
    main()