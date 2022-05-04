a,b,c = map(int, input().split())
n = int(input())
case = []
for _ in range(n):
  tp = 0
  for _ in range(3):
    d,e,f = map(int, input().split())
    tp += a * d + b * e + c * f
  case.append(tp)

print(max(case))