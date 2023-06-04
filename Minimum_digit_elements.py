def dig(n): 
    c=0
    while n!=0: 
        n=n//10
        c+=1
    return c
x = int(input())
l = list(map(int,input().split()))
a=[]
for i in l:
    a.append(dig(i))
    s = min(a)
print(a.count(s))