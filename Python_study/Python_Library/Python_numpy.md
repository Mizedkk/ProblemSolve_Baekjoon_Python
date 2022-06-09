# Data_scinece

## 📖 numpy란?

숫자와 관련된 파이썬 도구를 의미한다

### ✏️ 일반적인 배열 설정

```
# import numpy as np # np로 줄여서 많이 사용
import numpy
array1 = numpy.array([2,3,4,11,13,16,17,29,30])  # 배열 설정
array.shape # 어떤 형태인지 반환 
====================
(9,0)
```

<br>

### ✏️ full 함수를 이용한 설정
```
array1 = numpy.full(6, 7) # 7 원소로 6개 채워라
print(array1)
=======================
[7,7,7,7,7,7]
```

<br>

### ✏️ arrage 함수를 통한 배열 설정

```
import numpy as np
array1 = np.arange(10) # 0 ~ 9
array2 = np.arange(10,20) # 10 ~ 19
array1 + array2
=======================
[10, 12, 14, 16 ,18 ...]
```

<br>

### ✏️ numpy 배열을 이용한 boolean
```
import numpy as np
array1 = np.arange(10)
array > 4 # boolean 리스트 반환
======================
array[(False, False, False, False, False, True ...)]

booleans = np.array([False, False, False, False, False, True ...])
np.where(booleans)
# array([5, 6, 7, ...9])
```

<br>

### ✏️ numpy 의 기본통계
```
import numpy as np

array1 = np.array([14, 2, 3, 4, 5, 6])
print(np.max(array1)) # 최대값
print(np.min(array1)) # 최소값
print(np.mean(array1)) # 평균값
print(np.median(array1)) # 중앙값
print(np.std(array1)) # 표준 편차
print(np.var(array1)) # 분산

```


<br>


### ✏️ numpy vs python 

일반적으로 값을 추가하거나 빼는 경우에는 python을 사용하는 것이 좋으나
높은 수의 계산이나 복잡한 계산을 하는 경우에는 numpy을 사용하는 것이
시간이 빠르게 나온다 그에 따라 조절 해서 사용하는것을 추천한다.

<br>


