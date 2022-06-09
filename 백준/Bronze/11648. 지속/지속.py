st = input()
cnt = 0
while len(st) != 1:
    cnt += 1
    case = list(map(int, list(st)))
    num = 1
    for i in case:
        num *= i
    st = "".join(str(num))
print(cnt)