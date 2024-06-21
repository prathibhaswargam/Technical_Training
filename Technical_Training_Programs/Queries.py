n=int(input())
l=set()
res=[]
c=0
for i in range(n):
    a=input().split()
    x,y=a[0],a[1]
    if x=='1':
        l.add(y)
    elif x=='2':
        if y in l:
            res.append(True)
        else:
            res.append(False)
    elif x=='3':
        for j in l:
            if y in j:
                c+=1
        res.append(c)
    elif x=='4':
        if y in l:
            l.remove(y)
#print(l)
for i in res:
    print(i)

'''7
1 school
1 world
1 word
1 scholar
2 word
2 wood
3 sch
5
1 word
1 word
3 wo
4 word
2 word'''