#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #层序遍历计算
        if not root:
            return []
        from collections import deque
        que = deque([root])
        res = []
        while que:
            level = 0
            num = len(que)
            for _ in range(len(que)):
                cur = que.popleft()
                level+=cur.val
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            res.append(level/num)
        return res
# @lc code=end

