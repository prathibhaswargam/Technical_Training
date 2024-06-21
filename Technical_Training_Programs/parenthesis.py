def isValid(s):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or bracket_mapping[char] != stack.pop():
                return False
    return len(stack) == 0
str1=input("Enter parenthesis:")
print(isValid(str1))