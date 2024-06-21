l=list(map(int,input().split()))
'''n=len(l)//2
s=set()
for i in l:
    if l.count(i)>n and i not in s:
        print(i)
        s.add(i)'''

c=1
w=l[0]
for i in range(1,len(l)):
    if l[i]==w:
        c+=1
    elif l[i]!=w and c!=0:
        c-=1
    else:
        w=l[i]
    
print(w)