# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
val=input().split(" ")
res=[]
for i in range(1,len(val)+1,1):
    count=0
    for j in range(1,len(val)+1,1):
        if(val[i-1]==val[j-1]):
            count+=1
    res.append(count)
for k in range(1,len(val)+1,1):
    if(res[k-1]!=n):
        print(val[k-1])
        
