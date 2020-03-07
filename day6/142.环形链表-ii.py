#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None
        
# @lc code=end

class Node:
    def __init__(self, x=None, pos=None, next=None):
        self.val = x
        self.next = next
        self.pos = pos

class LinkedList(object):
    def __init__(self):
        self.root = Node()
        self.tailnode = None

    def append(self, value, pos):
        node = Node(x=value, pos=pos)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node

    def find(self, pos):
        for node in self.iter_node():
            if node.pos == pos:
                return node

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
    head = LinkedList()
    l = [-1,-7,7,-4,19,6,-9,-5,-2,-5]
    pos = 6
    for idx,v in enumerate(l):
        head.append(v, idx)

    print(list(head))
    node = head.find(pos)
    print(node.val)
    head.tailnode.next = node
    head.tailnode = node
    print(head.tailnode.pos)
    s = Solution()
    res = s.detectCycle(head.root.next)
    print(res.pos, res.val)



