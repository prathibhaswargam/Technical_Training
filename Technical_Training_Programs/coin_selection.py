coins = [1,3,5,6]
n = 11
d = [[9999] * (n+1) for _ in range(len(coins) + 1)]
for i in range(len(coins) + 1):
    d[i][0] = 0
for i in range(1, len(coins) + 1):
    for j in range(1, n + 1):
        if coins[i - 1] <= j:
            d[i][j] = min(d[i - 1][j], d[i][j - coins[i - 1]] + 1)
        else:
            d[i][j] = d[i - 1][j]
result = d[len(coins)][n]
if result == 9999:
    print("Not Possible")
else:
    print(f"Minimum coins for {n}: {result}")
for row in d:
    print(row)