n=int(input("Enter a no:"))
x=1
l=n*2-1
for i in range(l):
    for j in range(l):
        if i==n and j==n:
            print(i,end=" ")
        if i==0 or i==l-1 or j==0 or j==l-1:
            print(x,end=" ")
            x+=1
    print()