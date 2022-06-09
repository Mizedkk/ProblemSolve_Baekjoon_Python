case1 = []
case2 = []
for _ in range(10):
  case1.append(int(input()))
for _ in range(10):
  case2.append(int(input()))
case1.sort(reverse=True)
case2.sort(reverse=True)
W = sum(case1[:3])
K = sum(case2[:3])
print(W, K)