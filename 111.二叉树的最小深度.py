#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # res = []
        # cnt = 1
        
        # def dfs(node,cnt):
        #     if not node:
        #         return 
        #     if node.left is None and node.right is None:
        #         #叶子节点
        #         res.append(cnt)

        #     cnt+=1
        #     dfs(node.left,cnt)    
        #     dfs(node.right,cnt)
        # if not root:
        #     return 0   
        # dfs(root,cnt) 
        # # print(res)
        # return min(res)
        if not root:
            return 0
        from collections import deque
        que =deque([root])
        ans=0
        while que:
            ans+=1
            for _ in range(len(que)):
                cur = que.popleft()
                if cur.left is None and cur.right is None:
                    return ans
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return ans
# @lc code=end

