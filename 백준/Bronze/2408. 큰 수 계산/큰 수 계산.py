n = int(input())
cnt = 0
case = ""
for i in range(2*n - 1):
  case += input()

case = case.replace("/","//")
print(eval(case))
  