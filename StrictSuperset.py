A=list(map(int,input().split()))
n=int(input())
l=[]
for i in range(n):
   if all ((i in A for i in list(map(int,input().split())))):
    l.append(True)
   else:
    l.append(False)
print(all(l))