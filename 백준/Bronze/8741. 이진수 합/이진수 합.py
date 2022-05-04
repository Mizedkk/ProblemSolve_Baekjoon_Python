n = int(input())
k = 2 ** n - 1
answer = (k*(k+1))//2
answer = format(answer, "b")
print(answer)
