def fun(l1, l2, i=0, j=0, res=[]):
    if i == len(l1):
        return res
    if j == len(l2):
        return fun(l1, l2, i + 1, 0, res)
    if l1[i] % 2 == 0 and l2[j] % 2 != 0:
        res.append(l1[i] + l2[j])
    return fun(l1, l2, i, j + 1, res)
l1 = [6, 3, 2, 9, 4, 7]
l2 = [8, 7, 5, 3, 6, 9]
print(fun(l1, l2))
