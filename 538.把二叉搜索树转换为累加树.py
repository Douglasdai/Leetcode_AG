#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.pre = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #可以中序遍历累加然后倒转赋值

        #递归要右中左来遍历二叉树
        def sumup(node):
            if not node:
                return 
            sumup(node.right)
            node.val+=self.pre
            self.pre = node.val
            sumup(node.left)
        sumup(root)
        return root
# @lc code=end

