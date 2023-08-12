# Enter your code here. Read input from STDIN. Print output to STDOUT
inp=input().split(" ")
row=int(inp[0])
col=int(inp[1])
x=1
for i in range(1,row+1,1):
    if(i==((row+1)/2)):
        for j in range(1,int((col-7)/2)+1,1):
            print("-",end="")
        print("WELCOME",end="")
        for j in range(1,int((col-7)/2)+1,1):
            print("-",end="")
    elif(i<(row+1)/2):
        for j1 in range(1,int((row+1)/2)-i+1,1):
            print("---",end="")
        for j1 in range(1,x+1,1):
            print(".|.",end="")
        for j1 in range(1,int((row+1)/2)-i+1,1):
            print("---",end="")
        x=x+2;
    else:
        for j2 in range(1,i-int((row+1)/2)+1,1):
            print("---",end="") 
        for j2 in range(1,x-2+1,1):
            print(".|.",end="")
        for j2 in range(1,i-int((row+1)/2)+1,1):
            print("---",end="")
        x=x-2
    print()
               
    
