x=int(input())
l = list(map(int,input().split()))
c=0
for i in l:
    c+=i
    m = c//len(l)
for j in l:
    if m==j:
        print('True')
        break
else: print('False')