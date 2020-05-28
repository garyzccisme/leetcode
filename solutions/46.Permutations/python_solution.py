# BFS
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        bfs = [([], nums)]
        while bfs:
            pre, nex = bfs.pop(0)
            if len(nex) == 1:
                ans.append(pre + nex)
            else:
                for i in range(len(nex)):
                    bfs.append((pre + [nex[i]], nex[:i] + nex[i + 1:]))
        return ans

# DFS
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.dfs([], nums)
        return self.ans

    def dfs(self, pre, nex):
        if not nex:
            self.ans.append(pre)
        else:
            for i in range(len(nex)):
                self.dfs(pre + [nex[i]], nex[:i] + nex[i + 1:])