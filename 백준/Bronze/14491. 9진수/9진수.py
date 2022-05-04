n = int(input())

st = []

while not n < 1:
  a, b = divmod(n, 9)
  st.append(b)
  n = a
  
print("".join(map(str, st[::-1])))