def combination(l, i, j, k):
    a = []
    n = len(l)
    if i >= n - 2:
        return a
    if j >= n - 1 or j <= i:
        return combination(l, i + 1, i + 2, i + 3)
    if k >= n or k <= j:
        return combination(l, i, j + 1, j + 2)
    a.append([l[i], l[j], l[k]])
    return a + combination(l, i, j, k + 1)    
    
l=list(map(int,input("Enter a List:").split()))
'''n=len(l)
a=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a.append([l[i],l[j],l[k]])
print(a)'''
print(combination(l, 0, 1, 2))
            
'''def combination(l,k):
    def fun(curr, start):
        if len(curr) == k:
            print(curr)
            return
        for i in range(start, len(l)):
            fun(curr + [l[i]], i+1)

    fun([],0)
a = [3,2,5,4,1,6,8]
k=3
combination(a,k)'''