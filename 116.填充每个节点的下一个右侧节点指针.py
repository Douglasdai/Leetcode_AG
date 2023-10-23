#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #层次
        if not root:
            return root
        from collections import deque
        que = deque([root])
        while que:
            size = len(que)
            prev = None
            for i in range(size):
                cur = que.popleft()
                if prev:
                    prev.next = cur
                prev = cur 
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return root


        
# @lc code=end

