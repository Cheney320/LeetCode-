#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
class Solution:

    def orangesRotting(self, grid):
        m, n, time = len(grid), len(grid[0]), 0
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, time))
        
        # bfs
        while queue:
            i, j, time = queue.pop(0)
            directions = [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]
            for d in directions:
                if (d[0] >= 0 and d[0] < m) and (d[1] >= 0 and d[1] < n) and grid[d[0]][d[1]] == 1:
                    queue.append((d[0], d[1], time+1))
                    grid[d[0]][d[1]] = 2  # 标记为腐烂橘子

        for row in grid:
            if 1 in row: return -1

        return time

# @lc code=end

if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    s = Solution()
    print(s.orangesRotting(grid))