from collections import defaultdict


def f(n):
  if answer[n] != 0:
    return answer[n]
  
  answer[n] = f(n//p) + f(n//q)
  return answer[n]


if  __name__ == "__main__":
  answer = defaultdict(int)
  answer[0] = 1
  n, p, q = map(int, input().split())
  print(f(n))