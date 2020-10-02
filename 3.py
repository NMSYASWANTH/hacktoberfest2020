a=int(input())
for i in range(0,a):
    b=[int(x) for x in input().split()[:3]]
    c=int(input())
    if(c==0):
        d=sorted(b)
        print(*d)
    else:
        d=sorted(b)
        temp=d[0]
        d[0]=d[2]
        d[2]=temp
        print(*d)