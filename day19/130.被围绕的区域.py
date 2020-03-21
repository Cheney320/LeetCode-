#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# bfs非递归(借助队列)

# @lc code=start
class Solution:
    def bfs(self, i, j, board):
        row, col = len(board), len(board[0])
        queue = [(i, j)]
        while queue:
            i, j = queue.pop(0)
            if (i >= 0 and i < row) and (j >= 0 and j < col) and board[i][j] == 'O':
                board[i][j] = 'B'
                for x, y in [(-1,0), (1,0), (0,-1), (0, 1)]:
                    queue.append((i+x, j+y))

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        row, col = len(board), len(board[0])
        for i in range(row):
            if board[i][0] == 'O':
                self.bfs(i, 0, board)
            if board[i][col - 1] == 'O':
                self.bfs(i, col - 1, board)

        for j in range(col):
            if board[0][j] == 'O':
                self.bfs(0, j, board)
            if board[row - 1][j] == 'O':
                self.bfs(row - 1, j, board)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'

# @lc code=end

