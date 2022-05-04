case = "aeiouAEIOU"
while True:
  str = input()
  if str == "#": break
  count = 0
  for i in str:
    if i in case:
      count += 1
  print(count)