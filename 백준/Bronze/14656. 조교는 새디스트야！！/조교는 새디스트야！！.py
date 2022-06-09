import sys


def main():
  N = int(input())
  case = list(map(int, input().split()))
  cp_case = [i for i in range(1, N + 1)]
  cnt = 0
  for a, b in zip(case, cp_case):
    if a != b:
      cnt += 1

  print(cnt)


if __name__ == "__main__":
    main()