# DP
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = max(1 - dungeon[-1][-1], 1)

        for i in reversed(range(m - 1)):
            dp[i][-1] = max(dp[i + 1][-1] - dungeon[i][-1], 1)

        for j in reversed(range(n - 1)):
            dp[-1][j] = max(dp[-1][j + 1] - dungeon[-1][j], 1)

        for i in reversed(range(m - 1)):
            for j in reversed(range(n - 1)):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)

        return dp[0][0]

# DFS
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        self.m = len(dungeon)
        self.n = len(dungeon[0])
        self.dungeon = dungeon
        self.cache = [[0] * self.n for _ in range(self.m)]
        return self.dfs(0, 0)

    def dfs(self, i, j):

        if i == self.m - 1 and j == self.n - 1:
            self.cache[i][j] = max(1 - self.dungeon[i][j], 1)

        if self.cache[i][j]:
            return self.cache[i][j]

        down = right = float('inf')
        if i < self.m - 1: down = self.dfs(i + 1, j)
        if j < self.n - 1: right = self.dfs(i, j + 1)

        self.cache[i][j] = max(min(down, right) - self.dungeon[i][j], 1)
        return self.cache[i][j]

