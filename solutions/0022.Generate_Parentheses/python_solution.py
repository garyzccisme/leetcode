# DFS
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.dfs('', n, n)
        return self.ans

    def dfs(self, pre, left, right):
        if right == 0:
            self.ans.append(pre)
        if left:
            self.dfs(pre + '(', left - 1, right)
        if right > left:
            self.dfs(pre + ')', left, right - 1)

# BFS
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # For element in queue, it means (pre-string, left, right)
        queue = collections.deque([('', n, n)])
        while queue:
            pre, left, right = queue.popleft()
            if right == 0:
                ans.append(pre)
            if left:
                queue.append((pre + '(', left - 1, right))
            if right > left:
                queue.append((pre + ')', left, right - 1))
        return ans