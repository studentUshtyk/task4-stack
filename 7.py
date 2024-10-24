def longestValidParentheses(s: str) -> int:
    stack = [-1]  
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop() 
            if not stack:
                stack.append(i) 
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length
print(longestValidParentheses("(()"))      # Виведе 2
print(longestValidParentheses(")()())"))   # Виведе 4
print(longestValidParentheses(""))         # Виведе 0
