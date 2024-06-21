def isValid(s):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_mapping = {')': '(', ']': '[', '}': '{'}
    count=0
    for i in range(len(s)):
        if s[i] in opening_brackets:
            char=s[i]
            count+=1
            stack.append(char)
        elif s[i] in closing_brackets:
            char=s[i]
            count+=1
            if not stack or bracket_mapping[char] != stack.pop():
                return count
    if len(stack)==0:
        return 0
    else:
        return count+1
        
str1=input("Enter parenthesis:")
print(isValid(str1))
