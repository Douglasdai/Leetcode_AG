#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
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
        self.node = None
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #中序遍历，递归不用返回值
        # if root is None:
        #     node = TreeNode(val)
        #     return node 
        # if root.val <val:root.right = self.insertIntoBST(root.right,val)
        # if root.val>val:root.left = self.insertIntoBST(root.left,val)
        # return root

        #迭代法
        if root is None:
            node = TreeNode(val)
            return node 
        cur =root 
        parent = root 
        while cur is not None:
            parent = cur 
            if cur.val>val:
                cur = cur.left
            else:
                cur = cur.right
        node = TreeNode(val)
        #插入
        if parent.val<val:
            parent.right =node
        else:
            parent.left = node
        return root

# @lc code=end

