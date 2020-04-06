#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
利用前一个插入的位置进行提速，即每次先把当前要插入的元素和前一个插入点比较，
如果比它大，那么就从这里开始搜索，否则才需要从链表头开始搜索。
"""

class Solution:
    def insertionSortList(self, head):
        dummyHead = ListNode(0)
        preNode = dummyHead
        node = head
        while node:
            curNode = node
            node = node.next

            # 与前一个插入点比较决定从哪开始搜索
            if curNode.val < preNode.val:
                preNode = dummyHead
            while preNode.next and curNode.val > preNode.next.val:
                preNode = preNode.next
            curNode.next = preNode.next
            preNode.next = curNode

        return dummyHead.next


# @lc code=end

