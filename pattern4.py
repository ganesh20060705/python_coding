n=5 
k=5
for i in range(n):
    for j in range(n,i,-1):
        print(k,end=" ")
    print()
    k-=1