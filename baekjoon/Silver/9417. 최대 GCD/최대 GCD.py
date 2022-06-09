def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
for _ in range(int(input())):
    tmp=list(map(int, input().split()))
    ans=[]
    for i in range(len(tmp)):
        for j in range(i+1,len(tmp)):
          ans.append(gcd(max(tmp[i],tmp[j]),min(tmp[i],tmp[j]) ) )
    print(max(ans))
