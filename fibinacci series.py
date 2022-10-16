n=int(input("vallue of n:"))
a=1
b=1
c=0
if(n==1):
    print(a)
elif(n==2):
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(1,n,1):
        c=a+b
        print(c)
        a=b
        b=c
