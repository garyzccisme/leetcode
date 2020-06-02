# Expanding Method
class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Expand from i, j to find larger range
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - 1

        max_sub = ''
        for x in range(len(s)):
            # 2 palindrome cases
            for i, j in [(x, x), (x, x + 1)]:
                left, right = expand(i, j)
                if right - left + 1 > len(max_sub):
                    max_sub = s[left:right + 1]
        return max_sub

# DP
class Solution:
    def longestPalindrome(self, s: str) -> str:

        dp = [[0] * len(s) for _ in s]

        max_sub = ''
        for length in range(len(s)):
            i = 0
            while i + length < len(s):
                if s[i] == s[i + length]:
                    if length <= 1:
                        dp[i][i + length] = 1
                    else:
                        # Check left down value
                        dp[i][i + length] = dp[i + 1][i + length - 1]

                if dp[i][i + length] and length + 1 > len(max_sub):
                    max_sub = s[i:i + length + 1]
                i += 1

        return max_sub
