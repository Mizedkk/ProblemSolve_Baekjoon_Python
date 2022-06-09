import sys
import string

case = {}

for i in string.ascii_letters:
  case[i] = 0

st = sys.stdin.read()
for i in st:
  if i in case:
    case[i] += 1

answer = sorted(case.items(), key=lambda x: -x[1])
max_num = answer[0][1]

n = ''
for i in answer:
  if i[1] == max_num:
    n += i[0]

print(n)
