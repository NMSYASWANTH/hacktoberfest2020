a=int(input())
for i in range(0,a):
    d=[]
    e=[]
    b=int(input())
    c=[int(x) for x in input().split()[:b]]
    c=sorted(c)
    for i in range(0,len(c)):
        if(c[i]%2==0):
            d.append(c[i])
        else:
            e.append(c[i])
    print(*(d+e))
    
