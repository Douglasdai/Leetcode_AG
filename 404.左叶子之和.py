#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #递归精简版
        # if not root:
        #     return 0
        # leftval = 0
        # if root.left is not None and root.left.left is None and root.left.right is None:
        #     leftval = root.left.val
        # return leftval+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
        #迭代法遍历
        if not root:
            return 0
        stack = [root]
        ans=0
        while stack:
            node = stack.pop()
            if node.left and node.left.left is None and node.left.right is None:
                ans+=node.left.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        return ans
# @lc code=end

