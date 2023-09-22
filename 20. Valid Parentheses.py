class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:
                    return False
                if i ==')' and stack[-1] !='(' or i ==']' and stack[-1] !='[' or i =='}' and stack[-1] !='{':
                    return False
                stack.pop()
        if stack:
            return False
        else:
            return True
                