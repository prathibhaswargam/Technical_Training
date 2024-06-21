def anagram(s,n,a,i):
    if i>=n:
        return a
    x = input('Enter operation (L/R) and index: ').split()
    direction = x[0]
    index = int(x[1])
    if direction == 'L':
        shifted = s[index:] + s[:index]
    elif direction == 'R':
        shifted = s[-index:] + s[:-index]
    return anagram(shifted,index,a+s[0],i+1)
s=input('Enter a string:')
n=int(input())
x="".join(sorted(anagram(s,n,'',0)))
print(x)
l=[]
for i in range(n):
    l.append(s[i:n+i])
if x in l:
    print('Yes')
else:
    print('No')