x=int(input())
l = list(map(int,input().split()))
n = len(l)
c=0
for i in l: 
    c+=i
print(format(c/n,".2f" ))