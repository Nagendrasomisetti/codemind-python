def prime(i):
    if i==1:
        return 0
    for j in range(2,(i//2)+1):
        if i%j==0:
            return 0
    else: return 1
x = int(input())
m=[]
for i in range(1,x+1):
    if x%i==0:
        if prime(i):
            pass
        else:
            m.append(i)
print(len(m))