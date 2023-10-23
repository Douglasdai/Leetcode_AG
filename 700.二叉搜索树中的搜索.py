#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #继续递归
        # if not root:
        #     return 
        if val>root.val and root.right:
            return self.searchBST(root.right,val)
            #如果是叶子节点的话就返回null
        elif val<root.val and root.left:
            return self.searchBST(root.left,val)
        #记得val
        elif val==root.val:
            return root
        
# @lc code=end

