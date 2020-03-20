#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 深度优先递归
# 时间复杂度：访问每个节点一次，时间复杂度为O(N)，其中N为节点个数
# 空间复杂度：最坏情况下，整棵树是非平衡的，例如每个节点都只有一个孩子，递归
# 会调用N(树的高度)次，空间开销O(N)，最好的情况下，树是完全平衡的，高度只有log(N)，空间复杂度只有O(log(N))

class Solution:
    def minDepth(self, root):
        if not root: return 0
        children = [root.left, root.right]
        if not any(children): return 1
        mindepth = float('inf')
        for c in children:
            if c:
                mindepth = min(self.minDepth(c), mindepth)
        return mindepth + 1


# @lc code=end

