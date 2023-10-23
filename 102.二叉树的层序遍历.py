#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #递归方法
        # levels = []
        # def helper(node,level,levels):
        #     if not node:
        #         return 
        #     if len(levels)==level:
        #         levels.append([])
        #     levels[level].append(node.val)
        #     helper(node.left,level+1,levels)
        #     helper(node.right,level+1,levels)
        # helper(root,0,levels)
        # return levels
        
        #按照长度的方法
        from collections import deque
        if not root:
            return []
        que = deque([root])
        res = []
        while que:
            level = []
            for _ in range(len(que)):
                cur = que.popleft()
                level.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            res.append(level)
        return res
# @lc code=end

