class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.W = len(board[0])
        self.H = len(board)
        self.board = board

        for i in range(self.H):
            for j in range(self.W):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, word[1:]): return True
        return False

    def dfs(self, i, j, word):
        # Stop Condition
        if not word:
            return True

        # Mark visited point and store origin
        self.board[i][j], origin = -1, self.board[i][j]
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < self.H and 0 <= y < self.W and self.board[x][y] == word[0]:
                if self.dfs(x, y, word[1:]): return True

        # Revert the origin value
        self.board[i][j] = origin
        return False