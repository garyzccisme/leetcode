# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS with stack
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        self.ans = []
        odd_level = [root]
        even_level = []

        while odd_level or even_level:
            self.collect(odd_level, even_level, True)
            self.collect(even_level, odd_level, False)
        return self.ans

    def collect(self, cur_level, next_level, is_odd):
        level = []
        while cur_level:
            node = cur_level.pop()
            if node:
                level.append(node.val)
                # If current level is odd, next level starts from most right
                # If current level is even, next level starts from most left
                if is_odd:
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    next_level.append(node.right)
                    next_level.append(node.left)
        if level:
            self.ans.append(level)

# DFS
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.ans = []
        self.dfs(root, 0)
        return self.ans

    def dfs(self, node, level):
        if not node:
            return
        if level == len(self.ans):
            self.ans.append([node.val])
        else:
            if level % 2:
                self.ans[level].insert(0, node.val)
            else:
                self.ans[level].append(node.val)

        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)




