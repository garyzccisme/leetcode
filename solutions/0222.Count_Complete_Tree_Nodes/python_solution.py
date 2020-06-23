# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. Linear Time
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0

# 2. Better Solution
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.last_level_count = 0
        self.level = 0
        # Stop flag to end searching
        self.stop = 0

        # Start with -1 since the searching ends on the children of leafs (None)
        # Make -1 offset then self.level can be the real value
        self.dfs(root, -1)
        return 2 ** self.level - 1 + self.last_level_count // 2

    def dfs(self, node, level):
        if self.stop:
            return

        if not node:
            self.level = max(self.level, level - 1)
            # If the reaches the final level, then count 1
            # Note this is actually counting for # of children (None) of final level nodes
            if self.level == level:
                self.last_level_count += 1
            else:
                self.stop = 1
            return

        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)

# 3. Binary Search
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        # Find tree final level (Tree Height)
        self.root = root
        node = root
        self.level = -1
        while node:
            node = node.left
            self.level += 1

        # Start Binary Search
        left = 0
        right = 2 ** self.level - 1

        # If it's full binary tree then directly return # nodes
        if self.check_node(right):
            return 2 ** self.level + right

        while left < right - 1:
            mid = (left + right) // 2
            if self.check_node(mid):
                left = mid
            else:
                right = mid

        return 2 ** self.level + left

    def check_node(self, idx):
        node = self.root
        # The order if search path could be regarded as binary value converted from index
        # Make sure the len(order) = self.level
        order = format(idx, '0{}b'.format(self.level))
        for num in order:
            if num == '0':
                node = node.left
            else:
                node = node.right
        return True if node else False
