def isValid(self, s):
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif c == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif c == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0


# Intuition:
    # Use a stack to compare the current bracket to the one at the top of the stack.
    # Initialize a stack and loop through all the characters in the string.
    # If the current character is an opening bracket, then append it to the stack.
    # If it isn't (ie. it's a closing bracket), then first check if the stack has any elements.
    # If the stack doesn't, then return false because we have an extra closing bracket. (eg. '()]')
    # Otherwise, for all bracket types, check if the bracket at the top of the stack is an opening
    # bracket of the same type. If it is, pop from the stack. Otherwise, return false since the brackets
    # aren't closing in order.
    # Once the overarching loop breaks, return the result of the comparison of the length of the stack to
    # 0. If the length of the stack is not 0, then we had some extra braces. (eg. '[')

# Time complexity - O(n)
# Space complexity - O(n)