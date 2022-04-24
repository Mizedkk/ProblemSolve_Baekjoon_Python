#1,2학년 뉴비
#n학년 이하이면서 뉴비x = 올드비
#뉴비도 아니고 올비도 아니면 틀

n, m = map(int, input().split())

if m <= 2:
  print("NEWBIE!")
elif m <= n:
  print("OLDBIE!")
else:
  print("TLE!")