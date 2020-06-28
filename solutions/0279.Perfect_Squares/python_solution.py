# DP
class Solution:
    def numSquares(self, n: int) -> int:

        squares = [x ** 2 for x in range(1, int(n ** 0.5) + 1)]

        dp = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]


# Greedy DFS 1
class Solution:
    def numSquares(self, n: int) -> int:

        squares = [x ** 2 for x in range(int(n ** 0.5), 0, -1)]
        self.ans = float('inf')
        self.dfs(n, 0, squares)
        return self.ans

    def dfs(self, n, count, squares):
        if n == 0:
            self.ans = count
        else:
            for i, square in enumerate(squares):
                # Find the biggest square that is no larger than n
                # If current count is reaching second best answer, prune it
                if square <= n and count + 1 < self.ans:
                    self.dfs(n - square, count + 1, squares[i:])


# Greedy DFS 2
class Solution:
    def numSquares(self, n):

        def is_divided_by(n, count):
            """
                return: true if "n" can be decomposed into "count" number of perfect square numbers.
                e.g. n=12, count=3:  true.
                     n=12, count=2:  false
            """
            if count == 1:
                return n in square_nums

            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = set([i * i for i in range(1, int(n ** 0.5) + 1)])

        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count
