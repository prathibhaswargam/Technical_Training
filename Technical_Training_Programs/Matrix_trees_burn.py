def burn_trees(a, r, c):
    if r < 0 or r >= len(a) or c < 0 or c >= len(a[0]) or a[r][c] == 0:
        return 0
    if a[r][c] == 1:
        a[r][c]=2
        burn_trees(a, r + 1, c)
        burn_trees(a, r - 1, c)
        burn_trees(a, r, c + 1)
        burn_trees(a, r, c - 1)
    return a
n = int(input('Enter the number of rows: '))
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
r, c = map(int, input('Enter which row and which column tree burn: ').split())
b = burn_trees(a, r - 1, c - 1)
count=0
for i in range(n):
    for j in range(n):
        if b[i][j] == 1:
            count += 1
print("Number of unburnt trees:", count)