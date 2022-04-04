a, b = map(int, input().split())

def isprime(a, b):
  b += 1
  prime = [True] * b
  for i in range(2, int(b**0.5)+ 1):
    if prime[i]:
      for j in range(2 * i, b, i):
        prime[j] = False
  for i in range(a, b):
    if i > 1 and prime[i] == True:
      print(i)

isprime(a, b)