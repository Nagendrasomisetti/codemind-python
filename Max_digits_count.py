def dig(n):
    c=0 
    while(n): 
        n=n//10
        c+=1 
    return c
x = int(input())
l = list(map(int,input().split()))
a=[]
for i in range(x):
    a.append(dig(l[i]))
    s=max(a)
print(a.count(s))