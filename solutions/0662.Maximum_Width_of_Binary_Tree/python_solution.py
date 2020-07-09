# BFS
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        node_idx = [[]]
        # (node, level, index)
        nodes = collections.deque([(root, 0, 1)])
        ans = 0

        while nodes:
            node, level, idx = nodes.popleft()
            if len(node_idx) == level:
                # When starting with new level, calculate the nodes for last level
                ans = max(ans, node_idx[-1][-1] - node_idx[-1][0] + 1)
                # Append empty list to avoid index error
                node_idx.append([])
            if node:
                node_idx[level].append(idx)
                nodes.append((node.left, level + 1, 2 * idx - 1))
                nodes.append((node.right, level + 1, 2 * idx))

        return ans


# DFS
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.idx_dict = collections.defaultdict(list)
        # (node, level, index)
        self.dfs(root, 0, 1)

        return max([x[-1] - x[0] + 1 for x in self.idx_dict.values()])

    def dfs(self, node, level, idx):
        if node:
            self.idx_dict[level].append(idx)
            self.dfs(node.left, level + 1, idx * 2 - 1)
            self.dfs(node.right, level + 1, idx * 2)