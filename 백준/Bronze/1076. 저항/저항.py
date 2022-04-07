color = [["black", 0, 1], ["brown", 1, 10], ["red", 2, 100],["orange", 3, 1000], ["yellow", 4, 10000], ["green", 5, 100000], ["blue", 6, 1000000], ["violet", 7, 10000000], ["grey", 8, 100000000], ["white", 9, 1000000000]]

value = 0

for i in range(3):
  if i == 0:
    name = input()
    for j in color:
      if j[0] == name:
        value += 10 * j[1]
        break
      
  elif i == 1:
    name = input()
    for j in color:
      if j[0] == name:
        value += 1 * j[1]
        break
        
  else:
    name = input()
    for j in color:
      if j[0] == name:
        value *= j[2]
        break

print(value)