n=int(input())
def isprime(x, i=2):
    if x < 1:
        return False
    if i > x // 2:
        return True
    if x % i == 0:
        return False
    return isprime(x, i + 1)
f=0
for i in range(1,n):
    for j in range(i+1,n):
        if isprime(i) and isprime(j) and i+j==n:
            f=1
            break
if f==1:
    print(True)
else:
    print(False)