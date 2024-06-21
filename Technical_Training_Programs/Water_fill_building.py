l = [4, 9, 4, 5, 3, 2]
i = 0
s = 0
while i + 1 < len(l):
    if l[i] > l[i + 1]:
        d = 0
        for j in range(i + 1, len(l)):
            if l[j] >= l[i]:
                mini = min(l[i], l[j])
                units = j - i - 1
                s += mini * units - d
                i = j - 1
                break
            else:
                d += l[j]
        else:
            i += 1
    else:
        i += 1

print(s)
