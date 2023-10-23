#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #递归+分析情况
        if root is None:
            return root 
        if root.val ==key:
            #23，4，5
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right 
            elif root.right is None:
                return root.left
            else:
                #5
                cur = root.right 
                while cur.left is not None:
                    cur = cur.left
                cur.left = root.left
                return root.right 
        if root.val>key:
            root.left = self.deleteNode(root.left,key)
        if root.val<key:root.right = self.deleteNode(root.right,key)
        return root
# @lc code=end

