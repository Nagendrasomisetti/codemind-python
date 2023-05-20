p , r , t = list(map(int,input().split()))
m = p*((1+r/100)**t)
print(format(m,".2f" ))