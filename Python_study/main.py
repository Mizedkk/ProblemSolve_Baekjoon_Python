import re

p = re.compile('[a-z]+')
m = p.finditer("life is too short")
print(m)

for i in m:
    i.span()
