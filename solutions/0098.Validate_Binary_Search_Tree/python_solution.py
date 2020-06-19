# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, float('inf'), float('-inf'))

    def validate(self, node, upper, lower):
        if node is None:
            return True
        if lower < node.val < upper:
            return self.validate(node.left, node.val, lower) and self.validate(node.right, upper, node.val)
        else:
            return False
