#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def pathSum(self, root, sum):
        if not root: return []
        self.path.append(root.val)
        sum -= root.val
        if not root.left and not root.right and not sum:
            self.res.append(self.path[:])
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        self.path.pop()
        return self.res

# @lc code=end

