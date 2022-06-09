str = list(input().split())
if eval(f"{str[0]} + {str[2]}") == int(str[-1]):
  print("YES")
else:
  print("NO")