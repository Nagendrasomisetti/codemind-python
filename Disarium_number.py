x = int(input())
n = len(str(x))
b=x
s=0
while x!=0:
    v = x%10
    x = x//10
    m = v**n
    s+=m
    n-=1
if b==s:
    print("True")
else: print("False")