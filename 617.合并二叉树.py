#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #做起来比较好做，但是比较难理解，递归确定好就行
        if root1 is None: return root2
        if root2 is None: return root1
        root1.val +=root2.val6
        root1.left = self.mergeTrees(root1.left,root2.left)
        root1.right= self.mergeTrees(root1.right,root2.right)
        return root1
# @lc code=end

