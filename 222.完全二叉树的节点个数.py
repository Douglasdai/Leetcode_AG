#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #递归
        # if not root:
        #     return 0
        # return 1+self.countNodes(root.left)+self.countNodes(root.right)
        # #完全二叉树的递归 有一定的条件
        #先算深度，然后递归
        if not root:
            return 0
        left = root.left
        right = root.right
        ld,rd = 0,0
        while left:
            left = left.left
            ld+=1
        while right:
            right = right.right
            rd +=1
        if ld==rd:
            return (2<<ld)-1
        return self.countNodes(root.left)+self.countNodes(root.right)+1

#写法2
# class Solution: # 利用完全二叉树特性
#     def countNodes(self, root: TreeNode) -> int:
#         if not root: return 0
#         count = 1
#         left = root.left; right = root.right
#         while left and right:
#             count+=1
#             left = left.left; right = right.right
#         if not left and not right: # 如果同时到底说明是满二叉树，反之则不是
#             return 2**count-1
#         return 1+self.countNodes(root.left)+self.countNodes(root.right)  
# @lc code=end

