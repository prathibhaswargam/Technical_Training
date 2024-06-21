def alpha(s,a):
    d={}
    l=[]
    x=''
    for i in range(len(s)):
        d[s[i]]=i
    for i in a:
        l.append(d[i])
    l.sort()
    for i in range(len(l)):
        x+=get_key(l[i],d)
    return x
def get_key(val,my_dict): 
    for key, value in my_dict.items():
        if val == value:
            return key
def alpha1(s,a):
    x=''
    for i in s:
        if i in a:
            x+=i*a.count(i)
    return x
n=int(input('Enter no of outputs:'))
for i in range(n):
    s=input("Enter the alphabets:")
    a=input("Enter input:")
    print(alpha1(s,a))