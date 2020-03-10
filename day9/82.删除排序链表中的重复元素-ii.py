#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if not head: return head
        values = []   # 存储重复值
        p = head
        while p.next:
            if p.next.val == p.val:
                values.append(p.val)
            p = p.next
        # 删除节点
        dummyHead = ListNode(None)
        dummyHead.next = head
        prenode = dummyHead
        curnode = dummyHead.next
        while curnode:
            if curnode.val in values:
                prenode.next = curnode.next
                curnode = prenode.next
            else:
                prenode = curnode
                curnode = curnode.next
        return dummyHead.next
    
# @lc code=end

class LinkedList(object):
    def __init__(self):
        self.root = ListNode(None)
        self.tailnode = None

    def append(self, value):
        node = ListNode(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node


    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.val

if __name__ == "__main__":
    l = LinkedList()
    for i in [1,1,1,2,3]:
        l.append(i)
    print(list(l))
    s = Solution()
    head = s.deleteDuplicates(l.root.next)
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)
