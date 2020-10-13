class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:

        if len(A) != len(B):
            return False

        stack = []
        for i in range(len(A)):
            if A[i] != B[i]:
                if len(stack) >= 2:
                    return False
                else:
                    stack.append(i)

        if len(stack) == 0:
            return len(set(A)) != len(A)
        elif len(stack) == 2:
            if A[stack[0]] == B[stack[1]] and A[stack[1]] == B[stack[0]]:
                return True
            else:
                return False
        else:
            return False
