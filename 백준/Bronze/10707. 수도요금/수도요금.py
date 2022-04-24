A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

#제일 싼 수도요금 고르기
case1 = P * A
if P <= C:
  case2 = B
else:
  case2 = B + (P - C) * D

print(min(case1, case2))