# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative Solution
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root:
            return TreeNode(val)

        runner = root
        while True:
            if runner.val > val:
                if runner.left:
                    runner = runner.left
                else:
                    runner.left = TreeNode(val)
                    break
            else:
                if runner.right:
                    runner = runner.right
                else:
                    runner.right = TreeNode(val)
                    break
        return root


# Recursive Solution
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root:
            return TreeNode(val)

        self.dfs(root, val)
        return root

    def dfs(self, node, val):
        if node.val > val:
            if node.left:
                self.dfs(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self.dfs(node.right, val)
            else:
                node.right = TreeNode(val)