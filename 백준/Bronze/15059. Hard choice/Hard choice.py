a, b, c = map(int , input().split())
d, e, f = map(int , input().split())

sum = 0
if d - a > 0:
  sum += d - a
if e - b > 0:
  sum += e - b
if f - c > 0:
  sum += f - c

print(sum)