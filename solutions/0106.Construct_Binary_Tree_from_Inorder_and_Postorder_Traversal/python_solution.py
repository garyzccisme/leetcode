# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        root_index = inorder.index(root.val)

        right_inorder = inorder[root_index + 1:]
        left_inorder = inorder[:root_index]

        root.right = self.buildTree(right_inorder, postorder)
        root.left = self.buildTree(left_inorder, postorder)

        return root