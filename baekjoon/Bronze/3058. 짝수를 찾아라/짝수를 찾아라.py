n = int(input())

for _ in range(n):
  case = list(map(int, input().split()))
  case.sort()
  answer = [i for i in case if i % 2 == 0]
  print(sum(answer), answer[0])