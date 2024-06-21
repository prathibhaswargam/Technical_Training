#s=input('Enter a string:')
'''s=list(s)
a=[]
x=''
c=0
i=0
while(i<len(s)):
    if s[i] not in a:
        a.append(s[i])
        x+=s[i]
    else:
        if len(x)>c:
            c=len(x)
        b=s.index(s[i])
        b=b+1
        a=[]
        x=s[b]
        i=b
    i+=1
if len(a)>c:
    c=len(a)
print(c)'''
a=input()
d={}
m=0
i=0
s=''
while(i<len(a)):
    while(i<len(a)):
        if(a[i] not in s):
            s=s+a[i]
            d[s[i]]=i
        else:
            if(len(s)>m):
                m=len(s)
            s=""
            break
        i=i+1
    i=d[a[i]]+1
print(m)
0 1 1 1 0 1
0 1 0 1 0 0
1 0 1 1 0 0
0 0 0 1 1 1
1 1 0 0 0 1
1 1 1 0 1 0
