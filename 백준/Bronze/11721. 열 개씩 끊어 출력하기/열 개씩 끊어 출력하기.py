import sys

str = sys.stdin.readline()
while len(str) >= 10:
  print(str[0:10])
  str = str[10:]
print(str)