#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
思路：
交换一下左右节点，然后再递归的交换左节点，右节点。
- 终止条件：当前节点为null时返回
- 交换当前节点的左右节点，再递归的交换当前节点的左节点，递归的交换当前节点的右节点
时间复杂度：每个元素都必须访问一次，所以是O(n)
空间复杂度：最坏的情况下，需要存放O(h)个函数调用(h是树的高度)，所以是O(h)
"""

class Solution:
    def invertTree(self, root):
        if not root: return
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# @lc code=end

