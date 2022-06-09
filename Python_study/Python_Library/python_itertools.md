# itertools

##  ✏️ itertools 라이브러리 </p>
여러 반복객체에 관한 함수들을 다룬다.


## ✏️ permutations 함수
```
import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
# permutations(반복 가능한 객체, r)
```
순열을 구할때 사용한다. 

<br>

## ✏️ combinations 함수
```
import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))

결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]
# combinations(반복 가능한 객체, r)

```
조합을 구할때 사용한다. 

<br>

## ✏️ product 함수
```
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))
# 두 스트링 'ABCD', 'xy' 의 곱집합은 Ax Ay Bx By Cx Cy Dx Dy 입니다.

만약 리스트에서 n개를 뽑아서 중복순열을 구한다고 한다면, 

k = list(product(case, repeat=2))
repeat 이라는 것을 통해서 한다.
# product(반복 가능한 객체, repeat=1)
```
중복 순열을 구할때 사용되는 함수이다.

<br>

## ✏️ combinations_with_replacemnet 함수
```
from itertools import combinations_with_replacement

for cwr in combinations_with_replacement([1,2,3,4], 2):
    print(cwr, end=" ")
# combinations_with_replacement(반복 가능한 객체, r)
```
중복 조합을 만들때 사용한다.

<br>

## ✏️ cycle 함수
```
>>> import itertools
>>> emp_pool = itertools.cycle(['김은경', '이명자', '이성진'])
>>> next(emp_pool)
'김은경'
>>> next(emp_pool)
'이명자'
>>> next(emp_pool)
'이성진'
>>> next(emp_pool)
'김은경'

# next()는 파이썬 내장 함수로 이터레이터의 다음 요소를 반환한다.
```

<br>

## ✏️ accumulate 함수 
```
import itertools

monthly_income = [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
result = list(itertools.accumulate(monthly_income))

print(result)
========================
[1161, 2975, 4245, 6501, 7914, 9756, 11977, 14184, 16634, 19457, 21997, 24131]
```
각 리스트의 값을 점차 더해서 리턴해주는 함수이다.

<br>

## ✏️ zip_longest 함수 
```
import itertools

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
rewards = ['사탕', '초컬릿', '젤리']

result = itertools.zip_longest(students, rewards, fillvalue='새우깡')
print(list(result))
```
zip은 적은수의 객체를 기준으로 맞췄으나 이것은 더 많은 객체를 기준으로 맞추고 적은수의 객체가 다 돌았을 경우의 값을 fillvalue 값으로 채운다.

