a=int(input())
for i in range(0,a):
    b=int(input())
    for i in range(1,b+1):
        if(i%3==0):
            if(i%5==0):
                print("fizzbuzz",end="")
            else:
                print("fizz",end="")
        elif(i%5==0):
            print("buzz",end="")
        else:
            print(i,end="")
    print()
        
    