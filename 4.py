t=int(input())
f=0
for i in range (t):
    n,x=map(int,input().split())
    d=[int(e) for e in input().split()[:n]]
    for i in range (0,n):
        for j in range (i+1,n):
            if(d[i]+d[j]==x):
                f=f+1
    if(f>0):
        print("Yes")
    else:
        print("No")
        
    