# 알고리즘 수학

## 에라토스테네스의 체
에라토스테네스의 체는 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법이다.

<p align="center">
    <img src="Picture\Math_1.png">
</p>

1. 1을 제거한다.
2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다.
3. 지워지지 않은 수 중 제일 작은 3을 소수로 채택하고, 나머지 3의 배수를 모두 지운다.
4. ... 무한반복

이를 파이썬 코드로 표현하면 다음과 같다.
```
n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)
```

## 두 원사이의 관계
