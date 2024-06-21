n=input()
l=len(n)
a=''
if l%2==0:
    if int(n[:l//2]+n[:l//2:-1])>int(n):
        a=n[:l//2]+n[:l//2:-1]
    else:
        x=int(n[:l//2])+1
        x=str(x)
        a=x+x[::-1]
else:
    if int(n[:l // 2] + n[:l // 2:-1]) > int(n):
        a = n[:l // 2] + n[:l // 2:-1]
    else:
        x = int(n[:l // 2]) + 1
        x = str(x)
        a = x + x[::-1]
print(a)

