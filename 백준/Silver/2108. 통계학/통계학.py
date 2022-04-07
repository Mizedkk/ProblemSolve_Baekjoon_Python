import sys
import collections

n = int(sys.stdin.readline())
num = []
for i in range(n):
  num.append(int(sys.stdin.readline()))
num.sort()

#평균
print(round(sum(num)/n))
#중앙값
print(num[(n + 1)//2 - 1])
#최빈값
count_list = sorted(collections.Counter(num).items(), key = lambda x : (-x[1], x[0]))
if n == 1:
    print(num[0])
else:
    if count_list[0][1] != count_list[1][1]:
        print(count_list[0][0])
    else:
        print(count_list[1][0])
    
#범위
print(max(num) - min(num))
