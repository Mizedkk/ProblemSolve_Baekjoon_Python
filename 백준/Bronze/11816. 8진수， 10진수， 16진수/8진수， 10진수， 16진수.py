n = input()
if len(n) >= 2 and n[:2] == "0x":
  n = int(n[2:], 16)
elif len(n) >= 2 and n[0] == "0":
  n = int(n[1:], 8)
else:
  pass

print(n)
  