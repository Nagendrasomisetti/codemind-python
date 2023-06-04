x = list(map(str,input().split()))
m=0
for i in range(0,len(x)):
    if len(x[i])>m:
        m=len(x[i])
print(m)