class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for p in s:
            if p in pairs:
                stack.append(p)
            else:
                if not stack or p != pairs[stack.pop()]:
                    return False
        return stack == []