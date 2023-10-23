#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #中序后序遍历构造
        #还是按照递归的步骤
        #因为是后序 所以-1 为根节点，在中序中找到根节点的索引，左闭右开划分两个数组，然后进行建树
        # 第一步: 特殊情况讨论: 树为空. (递归终止条件)
        if not postorder:
            return None
        rootval  = postorder[-1]
        root = TreeNode(rootval)

        inorder_idx = inorder.index(rootval)
        #划分
        inorder_left = inorder[:inorder_idx]
        inorder_right = inorder[inorder_idx+1:]
        #根据长度划分
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):-1]
        
        #根节点
        root.left = self.buildTree(inorder_left,postorder_left)
        root.right = self.buildTree(inorder_right,postorder_right)
        return root
# @lc code=end

