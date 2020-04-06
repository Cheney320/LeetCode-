#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# 由于分配饼干这件事前后的步骤不会产生关联，所以根据贪心算法的原理，
# 分配的最优策略是每次分配只关注未分配饼干的最小胃口的小朋友。

# @lc code=start
class Solution:
    def findContentChildren(self, g, s):
        if not g or not s: return 0
        g.sort()
        s.sort()
        gi, si = 0, 0
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]: gi += 1
            si += 1
        return gi
        
# @lc code=end

