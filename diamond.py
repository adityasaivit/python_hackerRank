a=6
b=6
for i in range(1,6,1):
    for j in range(1,12,1):
        if((j>=a)&(j<=b)):
            print(" ",end="  ")
        else:
            print("*",end="  ")
    print("")
    a=a-1
    b=b+1
    
a=3
b=9
for k in range(1,5,1):
    for l in range(1,12,1):
        if((l>=a)&(l<=b)):
            print(" ",end="  ")
        else:
            print("*",end="  ")
    print("")
    a=a+1
    b=b-1
            

        
