#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                isEdge = i == 0 or j == 0 or i == m-1 or j == n-1
                if isEdge and board[i][j] == 'O':
                    self.dfs(board, i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

    
    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == 'X' or board[i][j] == '#':
            return
        board[i][j] = '#'
        self.dfs(board, i-1, j)  # 上
        self.dfs(board, i+1, j)  # 下
        self.dfs(board, i, j-1)  # 左
        self.dfs(board, i, j+1)  # 右


# @lc code=end

