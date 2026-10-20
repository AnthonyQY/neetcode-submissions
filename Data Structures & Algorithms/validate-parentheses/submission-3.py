class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_set = set(["(", "{", "["])

        for c in s:
            if c in open_set:
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == "}":
                    if stack[-1] != "{":
                        return False
                    else:
                        stack.pop()
                if c == ")":
                    if stack[-1] != "(":
                        return False
                    else:
                        stack.pop()
                if c == "]":
                    if stack[-1] != "[":
                        return False
                    else:
                        stack.pop()

        return True if len(stack) == 0 else False