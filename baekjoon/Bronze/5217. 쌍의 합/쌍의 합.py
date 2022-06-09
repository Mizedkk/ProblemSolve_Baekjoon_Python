import sys

test_case = int(sys.stdin.readline())
case = []

for _ in range(test_case):
  case.append(int(sys.stdin.readline()))

for i in case:
  print(f"Pairs for {i}:", end=" ")
  for j in range(1, i):
    if j >= i - j:
      break
    if j != 1:
      print(", ",end="")
    print(f"{j} {i - j}", end="")
  print("")