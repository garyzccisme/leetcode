class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # Stack here records invalid index
        stack = []
        ans = []
        for i, letter in enumerate(s):
            ans.append(letter)
            if letter in ('(', ')'):
                # Only Valid Case: stack[-1] is '(' and following by ')'
                if stack and s[stack[-1]] == '(' and letter == ')':
                    stack.pop()
                else:
                    stack.append(i)

        while stack:
            ans.pop(stack.pop())
        return ''.join(ans)
