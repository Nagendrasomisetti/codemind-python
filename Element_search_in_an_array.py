x=int(input())
l = list(map(int,input().split()))
n = int(input())
for i in l:
    if i == n:
        print('True')
        break
else: print('False')