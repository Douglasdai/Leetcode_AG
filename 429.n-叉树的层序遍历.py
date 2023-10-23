#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #层次遍历 儿子们
        if not root:
            return []
        from collections import deque
        que = deque([root])
        res = []
        while que:
            level = []
            for i in range(len(que)):
                cur = que.popleft()
                level.append(cur.val)
                for child in cur.children:
                    que.append(child)
            res.append(level)
        return res
# @lc code=end

