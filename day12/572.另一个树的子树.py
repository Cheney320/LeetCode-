#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s, t):
        def recur(s, t):
            if not t: return True
            if not s or s.val != t.val: return False
            return recur(s.left, t.left) and recur(s.right, t.right)

        return recur(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t) if s and t else False
        
# @lc code=end

