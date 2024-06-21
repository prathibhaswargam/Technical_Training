def fun(i, j, k):
    if k == len(word):
        return True
    if i < 0 or j < 0 or i >= n or j >= n or a[i][j] != word[k]:
        return False
    temp = a[i][j]
    a[i][j] = 0
    found = (fun(i + 1, j, k + 1) or
             fun(i - 1, j, k + 1) or
             fun(i, j + 1, k + 1) or
             fun(i, j - 1, k + 1))
    a[i][j] = temp
    return found

n = int(input('Enter no of rows: '))
a = []
for _ in range(n):
    a.append(input().split())
word = input('Enter the word to find: ')
found = False
for i in range(n):
    for j in range(n):
        if word[0] == a[i][j]:
            if fun(i, j, 0):
                found = True
                break
    if found:
        break

if found:
    print("Yes")
else:
    print("No")
