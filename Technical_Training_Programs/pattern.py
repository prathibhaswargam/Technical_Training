n=int(input('Enter a num:'))
c=1
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*',end=" ")
        else:
            print(c,end=" ")
            c+=1
    print()