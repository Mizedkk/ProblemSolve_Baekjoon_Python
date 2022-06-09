def sol(N):
  num = 1
  while True:
    if num % N == 0:
      break
    else:
      num = num*10 + 1
  return len(list(str(num)))

while True:
  try:
    N = int(input())
    print(sol(N))
  except:
    break