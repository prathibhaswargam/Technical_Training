n ='tu5g2k1h8'
m='g5g8gd6h3'
s=''
for i in n:
    if i.isnumeric():
        s+=i
for i in m:
    if i.isnumeric() and i not in s:
        s+=i
def combination(a, l, r):
    if l == r:
        if a[-1] % 2 == 0 and a[0]==max(s):
            res.append(int(''.join(map(str,a[:]))))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            combination(a, l + 1, r)
            a[l], a[i] = a[i], a[l]
    return res
res = []
s = list(map(int, s))
subsets = combination(s, 0, len(s) - 1)
print(max(subsets))
