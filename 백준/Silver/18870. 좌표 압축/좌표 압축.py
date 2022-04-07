import sys

# 반복
test_case = int(sys.stdin.readline())
# 테스트 케이스 입력
case = list(map(int, sys.stdin.readline().split()))
# 입력받은 케이스 중복제거 후 리스트 정렬 
index_case = sorted(list(set(case)))
# 인덱스 사전을 만들기
index = [i for i in range(test_case)]
index_dict = dict(zip(index_case, index))

# for문 안에서 list.index 접근할 경우 시간복잡도가 n^2 가됨
# 따라서 사전화 시켜서 접근한다면 시간복잡도 n 으로 줄일수 있음
for i in case:
  print(index_dict[i], end=" ")