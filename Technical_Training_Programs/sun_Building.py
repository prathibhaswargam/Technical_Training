l = [3, 5, 9, 6, 8, 10]
i = 0
j = len(l) - 1
c = 0
while i < len(l) - 1:
    if l[i+1] > l[i]:
        c += 1
    i += 1
print(c)
c=0
while j > 0:
    if l[j-1] > l[j]:
        c += 1
    if l[j] > l[j-1]:
        c += 1
        break
    j -= 1
print(c)

