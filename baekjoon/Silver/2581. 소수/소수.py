def dtm(num):
  for i in range(2, num):
    if num % i == 0:
      return;
  return num;

m = int(input())
n = int(input())
case = []
if n == 1:
  print(-1)  
else:
  if m == 1:
    m = 2
  for i in range(m, n+1):
    case.append(dtm(i))
  case = list(filter(None, case))
  if len(case) == 0:
    print(-1)
  else:
    print(sum(case))
    print(min(case))