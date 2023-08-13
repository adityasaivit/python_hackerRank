n=int(input())
record=[]
for i in range(1,n+1,1):
    l1=input().split(" ")
    record.append(l1)
inp=input()
for j in range(1,n+1,1):
    if(record[j-1][0]==inp):
        avg=(float(record[j-1][1])+float(record[j-1][2])+float(record[j-1][3]))/3
        print(format(avg,".2f"))
            
