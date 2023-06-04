x = list(map(str,input().split()))
a=[]
for i in x:
    c=0
    for j in i:
        c+=1
    a.append(c) 
    c=0
print(min(a))