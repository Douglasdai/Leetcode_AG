#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        # def dfs(node):
        #     if not node:
        #         return 
            
        #     dfs(node.left)
        #     dfs(node.right)
        #     ans.append(node.val)
        # dfs(root)
        # return ans
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        #将数组反转
        return ans[::-1]
# @lc code=end

