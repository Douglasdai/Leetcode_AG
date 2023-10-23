#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # cnt =0
        # ans = []
        # def dfs(node,cnt):
        #     if not node:
        #         #叶子节点
        #         ans.append(cnt)
        #         #重置
        #         cnt = 0
        #         return ans
        #     # if node.left is None and node.right is None:  
        #     cnt+=1
        #     dfs(node.left,cnt)
        #     dfs(node.right,cnt)
        # dfs(root,cnt)
        # return max(ans)
        #层次遍历
        if not root:
            return 0
        from collections import deque
        que = deque([root])
        ans = 0
        while que:
            for _ in range(len(que)):
                cur =que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            ans+=1
        return ans

# @lc code=end


