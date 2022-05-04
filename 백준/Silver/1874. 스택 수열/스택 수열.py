import sys
n = int(sys.stdin.readline())

temp = True
stack = []
answer = []
count = 1

for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        answer.append('+')
        count += 1
    if stack[-1] == num: 
        stack.pop()
        answer.append('-')
    else:
        temp = False
        
if not temp:
    print('NO')
else:
    for i in answer:
        print(i)