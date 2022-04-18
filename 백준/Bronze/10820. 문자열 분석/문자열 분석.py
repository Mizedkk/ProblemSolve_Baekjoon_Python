import string


try:
  while True:
    low_case = 0
    up_case = 0
    digit = 0
    space = 0
    str = input()
    for i in str:
      if i in string.ascii_lowercase:
        low_case += 1
      elif i in string.ascii_uppercase:
        up_case += 1
      elif i in string.digits:
        digit += 1
      elif i == " ":
        space += 1
    print(low_case, up_case, digit, space)


  
except:
  pass