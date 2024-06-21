def generate_parentheses(n):
    def backtrack(combination, left, right):
        #print("combination:",combination,'left:',left,'right:',right)
        if left < n:
            backtrack(combination + '(', left + 1, right)
        if right < left:
            backtrack(combination + ')', left, right + 1)
        if left < n:
            backtrack(combination + '[', left + 1, right)
        if right < left:
            backtrack(combination + ']', left, right + 1)
        if left < n:
            backtrack(combination + '{', left + 1, right)
        if right < left:
            backtrack(combination + '}', left, right + 1)
        if left==n and right==n:
            combinations.append(combination)
            return 
    combinations = []
    backtrack('', 0, 0)
    return combinations

n = int(input("Enter the number of pairs: "))
result = generate_parentheses(n)

for combination in result:
    print(combination)
