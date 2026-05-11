class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) == 1:
            return False

        for x in s:
            if x in ["(","[","{"]:
                stack.append(x)
            elif x == ")":
                if len(stack) == 0:
                    return False
                if stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif x == "]":
                if len(stack) == 0:
                    return False
                if stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            elif x == "}":
                if len(stack) == 0:
                    return False
                if stack[-1] != "{":
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True