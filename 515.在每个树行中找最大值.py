#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        #层序 遍历 找max
        if not root:
            return []
        from collections import deque
        import sys
        que = deque([root])
        res = []
        while que:
            level =-sys.maxsize-1 
            # cur =que.popleft()
            for _ in range(len(que)):
                cur =que.popleft()
                level= max(level,cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            res.append(level)
        return res



# @lc code=end

