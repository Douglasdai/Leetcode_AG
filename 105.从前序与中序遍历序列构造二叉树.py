#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #跟106一样只不过后序换成了前序
        if not preorder:
            return 
        rootval = preorder[0]
        root = TreeNode(rootval)

        inorder_idx = inorder.index(rootval)
        inorder_left = inorder[:inorder_idx]
        inorder_right = inorder[inorder_idx+1:]
        #舍去前面的一个
        preorder_left = preorder[1:len(inorder_left)+1]
        preorder_right = preorder[len(inorder_left)+1:]

        root.left = self.buildTree(preorder_left,inorder_left)
        root.right= self.buildTree(preorder_right,inorder_right)
        return root

# @lc code=en
# d

