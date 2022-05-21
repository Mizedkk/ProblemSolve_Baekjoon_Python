def main():
    num = int(input())
    num = format(num, "b")
    num = int(str(num)[::-1], 2)
    print(num)


if __name__ == "__main__":
    main()