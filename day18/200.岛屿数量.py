#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# 深度优先搜索
# 线性扫描整个二维网格，如果一个结点包含 1，则以其为根结点启动深度优先搜索。
# 在深度优先搜索过程中，每个访问过的结点被标记为 0。计数启动深度优先搜索的根结点的数量，即为岛屿的数量。

# @lc code=start
class Solution:
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        # i和j判断是否越界，grid[i][j] == '0'有两种情况，一是代表结点为水域，而是代表该结点访问过。碰到越界和0的情况则返回。
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'   # 0标记访问过的结点
        # 从当前结点的上下左右四个方向继续访问
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)


    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    self.dfs(grid, i, j)
        return num_islands


# @lc code=end


if __name__ == "__main__":
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    s = Solution()
    print(s.numIslands(grid))

