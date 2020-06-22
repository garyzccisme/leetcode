# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        self.ans = []
        self.dfs(root, 0)
        return self.ans

    def dfs(self, node, level):
        if not node:
            return

        if level == len(self.ans):
            self.ans.append([node.val])
        else:
            self.ans[level].append(node.val)

        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)

# BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        ans = []
        queue = collections.deque([(root, 0)])

        while queue:
            node, level = queue.popleft()
            if node:
                if level == len(ans):
                    ans.append([node.val])
                else:
                    ans[level].append(node.val)

                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

        return ans