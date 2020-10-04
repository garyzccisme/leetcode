class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.ans = []
        self.dfs(target, cur=[], k=0)
        return self.ans

    def dfs(self, target, cur, k):
        if target == 0:
            self.ans.append(cur)
        elif target > 0 and k < len(self.candidates):
            for i in range(k, len(self.candidates)):
                self.dfs(target - self.candidates[i], cur + [self.candidates[i]], i)
