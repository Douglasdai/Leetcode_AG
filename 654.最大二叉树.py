#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        #递归+划分
        if not nums:return 
        ans = max(nums)
        root_idx = nums.index(ans)
        root = TreeNode(ans)
        #左边的
        bulid_left = nums[:root_idx]
        #右边的
        bulid_right = nums[root_idx+1:]
        root.left = self.constructMaximumBinaryTree(bulid_left)
        root.right = self.constructMaximumBinaryTree(bulid_right)
        return root

# @lc code=end

