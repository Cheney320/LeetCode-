# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 广度优先搜索(BFS)，借助队列先入先出特性实现。
# 时间复杂度O(N):N为二叉树的节点数量，即BFS需循环N次。
# 空间复杂度O(N):最差情况下，即当树为平衡二叉树时，最多有N/2个树节点同时在queue中，使用O(N)大小的额外空间。
class Solution:
    def levelOrder(self, root):
        if not root: return []
        res, queue = [], [root]
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res