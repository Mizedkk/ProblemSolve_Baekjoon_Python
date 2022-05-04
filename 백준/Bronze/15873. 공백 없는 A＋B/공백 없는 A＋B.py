n = input()
if n[1] == "0":
  print(eval(f"{n[:2]} + {n[2:]}"))
else:
  print(eval(f"{n[0]} + {n[1:]}"))