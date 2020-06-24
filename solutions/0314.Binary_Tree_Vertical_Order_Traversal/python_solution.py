# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans_dict = collections.defaultdict(list)
        node_queue = collections.deque([(root, 0)])
        min_idx = max_idx = 0

        while node_queue:
            node, idx = node_queue.popleft()
            ans_dict[idx].append(node.val)

            min_idx = min(min_idx, idx)
            max_idx = max(max_idx, idx)

            if node.left:
                node_queue.append((node.left, idx - 1))
            if node.right:
                node_queue.append((node.right, idx + 1))

        ans = [ans_dict[key] for key in range(min_idx, max_idx + 1)]
        return ans