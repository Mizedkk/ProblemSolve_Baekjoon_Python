start = input()
case = []
while True:
  st = input()
  if st == "고무오리 디버깅 끝":
    break
  elif st == "문제":
    case.append(1)
  elif st == "고무오리":
    try:
      case.pop()
    except:
      case.append(1)
      case.append(1)

if len(case) == 0:
  print("고무오리야 사랑해")
else:
  print("힝구")