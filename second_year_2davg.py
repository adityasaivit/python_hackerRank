inp=input().split(" ")
marks=[]
for i in range(1,int(inp[1])+1,1):
    val=input().split(" ")
    marks.append(val)
avg=[]
for j in range(1,int(inp[0])+1,1):
    sum=0
    for k in range(1,int(inp[1])+1,1):
        sum=sum+float(marks[k-1][j-1])
    avg.append(sum/int(inp[1]))
for k1 in avg:
    print(k1)
