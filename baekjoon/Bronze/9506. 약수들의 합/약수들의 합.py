while True:
  n = int(input())
  if n == -1 : break
  case = []
  for i in range(1, n//2 + 1):
    if n % i == 0:
      case.append(i)
  
  if sum(case) == n:
    case = list(map(str, case))
    st = " + ".join(case)
    print(f"{n} = {st}")
  else:
    print(f"{n} is NOT perfect.")