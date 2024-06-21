def anagram(s, n, a, i):
    if i >= n:
        return a
    operation = input('Enter operation (L/R) and index: ').split()
    direction = operation[0]
    index = int(operation[1])
    if direction == 'L':
        shifted = s[index:] + s[:index]
    elif direction == 'R':
        shifted = s[-index:] + s[:-index]
    
    return anagram(shifted, n, a + shifted, i + 1)
s = input('Enter a string: ')
n = int(input('Enter the number of operations: '))
result = anagram(s, n, '', 0)
target = ''.join(sorted(result))
substrings = []
for i in range(len(s) - len(target) + 1):
    substrings.append(s[i:i+len(target)])
if target in substrings:
    print('Yes')
else:
    print('No')

