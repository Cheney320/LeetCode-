#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def get_length(self, head):
        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        return length

    # cut函数将链表head切掉前n个节点，并返回后半部分的链表头
    def cut(self, head, n):
        p = head
        while p and n:
            p = p.next
            n -= 1

        if not p: return None

        next = p.next
        p.next = None
        return next
    

    def merge(self, left, right):
        dummyHead = ListNode(None)  # 虚拟头
        p = dummyHead
        while left and right:
            if left.val < right.val:
                p.next = left
                p = left
                left = left.next
            else:
                p.next = right
                p = right
                right = right.next
        p.next = left if left else right
        return dummyHead.next  # 返回排序后的结果

    def sortList(self, head):
        dummyHead = ListNode(None)
        dummyHead.next  = head
        sz = 0
        n = self.get_length(head)
        while sz <= n:
            cur = dummyHead.next
            tail = dummyHead
            while cur:
                left = cur
                right = self.cut(left, sz)   # left->@->@ right->@->@->@...
                cur = self.cut(right, sz)  # left->@->@ right->@->@ cur->@->...
                tail.next = self.merge(left, right)
                while tail.next:
                    tail = tail.next
            sz = sz*2 + 1
        return dummyHead.next

# @lc code=end

