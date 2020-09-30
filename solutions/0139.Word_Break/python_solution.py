# Memoization DFS
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.str_dict = {}
        return self.dfs(s, wordDict)

    def dfs(self, s, wordDict):
        if s == '':
            return True
        if s in self.str_dict:
            return self.str_dict[s]
        for word in wordDict:
            if s.startswith(word):
                res = self.dfs(s[len(word):], wordDict)
                if res:
                    return res
        self.str_dict[s] = False
        return False

# DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
                if len(word) <= i + 1 and s[:i + 1].endswith(word) and dp[i + 1 - len(word)]:
                        dp[i + 1] = True

        return dp[-1]