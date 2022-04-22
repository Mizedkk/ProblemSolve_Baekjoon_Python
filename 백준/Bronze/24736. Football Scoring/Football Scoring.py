answer = []
for _ in range(2):
  case = list(map(int ,input().split()))
  answer.append(6 * case[0] + 3 * case[1] + 2 * case[2] + case[3] + 2 * case[4])
print(*answer)