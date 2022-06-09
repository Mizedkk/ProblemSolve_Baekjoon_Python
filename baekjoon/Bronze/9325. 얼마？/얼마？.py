n = int(input())
for _ in range(n):
  car = int(input())
  car_n = int(input())
  for _ in range(car_n):
    q, p = map(int, input().split())
    car += q * p
  print(car)