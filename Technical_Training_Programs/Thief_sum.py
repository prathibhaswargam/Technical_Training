def Thief_sum(l, i, s):
    if i >= len(l):
        return s
    return max(Thief_sum(l, i + 1, s), Thief_sum(l, i + 2, s + l[i]))
n = list(map(int, input().split()))
print(Thief_sum(n,0,0))
