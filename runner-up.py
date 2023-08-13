n=int(input())
score=input().split(" ")
scorea=[]
for x in range(1,n+1,1):
    scorea.append(int(score[x-1]))
maximum=max(scorea)

count=0
for i in scorea:
    if(i==maximum):
        count+=1
for j in range(1,count+1,1):
    scorea.remove(maximum)
print(max(scorea))
