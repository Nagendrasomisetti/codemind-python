def prime(j):
    i=2
    v=0
    while i!=j:
        if j%i==0:
            v=1
        i+=1
    if v==0:
        return j
def is_palin(j):
    m = j
    s=0
    while m!=0:
        v = m%10
        s = s*10+v 
        m = m//10
    if j==s:
        return j
x = int(input())
g = x+1
while g!=0:
    if is_palin(g):
        if prime(g):
            print(g)
            break
    g+=1