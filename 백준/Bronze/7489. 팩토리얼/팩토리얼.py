import math
import re

n = int(input())
for _ in range(n):
    num = int(input())
    answer = str(math.factorial(num))
    i = -1
    while True:
        if answer[i] != "0":
            print(answer[i])
            break
        else:
            i -= 1