#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 迭代法(使用栈),时间复杂度O(n),空间复杂度O(n)
class Solution:
    def isValidBST(self, root):
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root: continue

            val = root.val
            if val <= lower or val >= upper:
                return False
            
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
        
# @lc code=end

