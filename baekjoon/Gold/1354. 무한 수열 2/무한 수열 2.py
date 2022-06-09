from collections import defaultdict


def f(n):
  if answer[n] != 0 :
    return answer[n]
  elif n < 0:
    return 1
  
  answer[n] = f(n//p - x) + f(n//q - y)
  return answer[n]


if  __name__ == "__main__":
  answer = defaultdict(int)
  answer[0] = 1
  n, p, q, x, y = map(int, input().split())
  print(f(n))