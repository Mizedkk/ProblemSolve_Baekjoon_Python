a,b,c = map(int, input().split())
print(sum([max(a,b,c) - a,max(a,b,c) - b,max(a,b,c) - c]))