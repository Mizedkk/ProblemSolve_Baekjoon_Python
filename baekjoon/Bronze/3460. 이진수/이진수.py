test_case = int(input())
for _ in range(test_case):
  num = int(input())
  num = format(num, "b")

  num = str(num)[::-1]
  for i in range(len(num)):
    if num[i] == "1":
      print(i, end=" ")
  print("")
    