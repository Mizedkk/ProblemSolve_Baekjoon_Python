import sys


def main():
  N = int(sys.stdin.readline())
  for i in range(1, N + 1):
    if i == 1:
      print(" " * (N - i) + "*")
    else:
      print(" " * (N - i) + "*" + " " * (2*i - 3) + "*")


if __name__ == "__main__":
    main()