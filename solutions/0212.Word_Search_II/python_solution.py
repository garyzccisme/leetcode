# Official Solution
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):

            letter = board[row][col]
            currNode = parent[letter]

            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)

            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = '#'

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            # End of EXPLORATION, we restore the cell
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords


# My Solution
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Build trie according to given words
        trie = {}
        self.word_mark = '$'
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[self.word_mark] = word

        self.ans = []
        self.board = board
        self.M = len(board)
        self.N = len(board[0])

        for i in range(self.M):
            for j in range(self.N):
                if board[i][j] in trie:
                    node = trie
                    self.dfs(i, j, trie)

        return self.ans

    def dfs(self, i, j, node):

        letter = self.board[i][j]
        node = node[letter]

        # Must use pop to avoid duplicate word
        word = node.pop(self.word_mark, False)
        # If find word_mark then append to self.ans
        # Note: this is not finished, continue searching until node is empty
        if word:
            self.ans.append(word)

        self.board[i][j] = '*'
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < self.M and 0 <= y < self.N and self.board[x][y] in node:
                self.dfs(x, y, node)

        # Revert origin value
        self.board[i][j] = letter
