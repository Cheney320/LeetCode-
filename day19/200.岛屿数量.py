#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# 广度优先搜索
# 线性扫描整个二维网格，如果一个结点包含 1，则以其为根结点启动广度优先搜索。
# 将其放入队列中，并将值设为 0 以标记访问过该结点。迭代地搜索队列中的每个结点，直到队列为空。

# @lc code=start
class Solution:
    def bfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        queue = [(i, j)]
        grid[i][j] = '0'  # 标记访问过
        while queue:
            i, j = queue.pop(0)
            directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for d in directions:
                if (d[0] >= 0 and d[0] < m) and (d[1] >= 0 and d[1] < n) and grid[d[0]][d[1]] == '1':
                    queue.append((d[0], d[1]))
                    grid[d[0]][d[1]] = '0'   # 标记访问过

    def numIslands(self, grid):
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        island_num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island_num += 1
                    self.bfs(grid, i, j)
        return island_num

# @lc code=end


if __name__ == "__main__":
    # grid = [['1', '1', '1', '1', '0'],
    #         ['1', '1', '0', '1', '0'],
    #         ['1', '1', '0', '0', '0'],
    #         ['0', '0', '0', '0', '0']]
    grid = [['1','1','0','0','0'],
            ['1','1','0','0','0'],
            ['0','0','1','0','0'],
            ['0','0','0','1','1']]
    s = Solution()
    print(s.numIslands(grid))
