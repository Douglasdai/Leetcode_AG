#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #层序把最后一个放入到res 中
        if not root:
            return []
        res = []
        from collections import deque
        que =deque([root])
        while que:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                if i==size-1:
                    res.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return res

# @lc code=end

