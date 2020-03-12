#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start

# Definition for a Node.

"""
方法一：深度优先搜索(时间复杂度O(N),空间复杂度O(n))
1. 从头结点 head 开始拷贝；
2. 由于一个结点可能被多个指针指到，因此如果该结点已被拷贝，则不需要重复拷贝；
3. 如果还没拷贝该结点，则创建一个新的结点进行拷贝，并将拷贝过的结点保存在哈希表中；
4. 使用递归拷贝所有的 next 结点，再递归拷贝所有的 random 结点。

方法二：优化的迭代(时间复杂度O(n),空间复杂度O(1))
遍历链表两次：
第一遍：把每个新生成的结点放在对应的旧结点后面， 形如: 1->1'->2->2'->3->3'->4->4'->null。
第二遍：修改每个新结点的 next 指针和 random 指针。
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # def dfs(self, head, visited):
    #     if not head: return None
    #     if head in visited:
    #         return visited[head]
    #     # 创建新结点
    #     copy = Node(head.val)
    #     visited[head] = copy
    #     copy.next = self.dfs(head.next, visited)
    #     copy.random = self.dfs(head.random, visited)
    #     return copy
        
    # def copyRandomList(self, head):
    #     visited = {}
    #     return self.dfs(head, visited)

    def copyRandomList(self, head):
        if not head: return None
        # 第一遍遍历，把每个新生成的结点放在对应的旧结点后面
        p = head
        while p:
            new_node = Node(p.val)
            new_node.next = p.next
            p.next = new_node
            p = new_node.next    # 下一个旧结点

        # 第二遍修改每个新结点的next和random
        p = head
        while p:
            next_origin = p.next.next   # 下一个旧结点备份一下
            p.next.next = next_origin.next if next_origin else None  # 修改新结点的next
            p.next.random = p.random.next if p.random else None
            p = next_origin  # 下一个旧结点
        
        return head.next
        
# @lc code=end

