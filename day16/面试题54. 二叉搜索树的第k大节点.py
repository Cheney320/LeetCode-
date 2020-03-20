# 中序遍历(左根右)
class Solution:
    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

    def kthLargest(self, root, k):
        res = self.inorder(root)
        return res[-k]