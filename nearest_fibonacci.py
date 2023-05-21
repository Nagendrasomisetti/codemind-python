def fib(x):
    a=0
    b=1
    c=a+b
    while c<x:
        c=a+b
        a,b=b,c 
    if x==c: 
        return x
x = int(input())
a=x
for i in range(x,1,-1):
    if fib(i):
        n=i
        break
while x!=0:
    if fib(x):
        m=x 
        break 
    x+=1
if (a-n)<(m-a):
    print(n)
elif (a-n)==(m-a):
    print(n,m)
else: print(m)