a=int(input())
b=[int(x) for x in input().split()[:a]]
c=0
d=0
e=0
for i in range(0,a):
    if(b[i]<0):
        c=c+1
    if(b[i]>0):
        d=d+1
    if(b[i]==0):
        e=e+1
print("{0:.6f}".format(d/a)) 
print("{0:.6f}".format(c/a))
print("{0:.6f}".format(e/a))
