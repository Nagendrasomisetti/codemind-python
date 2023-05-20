x = eval(input())
n=0
for y in range(1,x):
    if x%y==0:
        n+=y
if n==x:
    print("True" )
else:
    print("False" )