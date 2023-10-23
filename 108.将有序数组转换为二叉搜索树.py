#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #递归 类似于二分法
        def bulirdTree(nums,left,right):
            if left>right:
                return None
            mid = left+(right-left)//2
            root = TreeNode(nums[mid])
            root.left = bulirdTree(nums,left,mid-1)
            root.right = bulirdTree(nums,mid+1,right)
            return root 
        root = bulirdTree(nums,0,len(nums)-1)
        return root
# @lc code=end

