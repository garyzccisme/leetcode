# DFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        """

        if not board or len(board) == 1:
            return

        self.W = len(board[0])
        self.H = len(board)

        # Check border to find static 'O'
        for i in range(self.H):
            for j in (0, self.W - 1):
                if board[i][j] == 'O':
                    self.dfs(i, j, board)
        for i in (0, self.H - 1):
            for j in range(self.W):
                if board[i][j] == 'O':
                    self.dfs(i, j, board)

        # Start Change
        for i in range(self.H):
            for j in range(self.W):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'

    def dfs(self, i, j, board):
        # Mark static 'O' as 'V'
        board[i][j] = 'V'
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < self.H and 0 <= y < self.W and board[x][y] == 'O':
                self.dfs(x, y, board)

# BFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        """

        if not board or len(board) == 1:
            return

        self.W = len(board[0])
        self.H = len(board)

        static_list = []

        # Check border to find static 'O'
        for i in range(self.H):
            for j in (0, self.W - 1):
                if board[i][j] == 'O':
                    static_list.append((i, j))
        for i in (0, self.H - 1):
            for j in range(self.W):
                if board[i][j] == 'O':
                    static_list.append((i, j))

        # Mark static 'O' as 'V'
        while static_list:
            i, j = static_list.pop(0)
            board[i][j] = 'V'
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < self.H and 0 <= y < self.W and board[x][y] == 'O':
                    static_list.append((x, y))

        # Start Change
        for i in range(self.H):
            for j in range(self.W):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'