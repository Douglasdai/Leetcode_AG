#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #自底向上递归
        # def recur(root):
        #     if not root: return 0
        #     left = recur(root.left)
        #     if left == -1: return -1
        #     right = recur(root.right)
        #     if right == -1: return -1
        #     return max(left, right) + 1 if abs(left - right) <= 1 else -1

        # return recur(root) != -1
 
        #需要后序遍历
        #递归
        # if not root:
        #     return 0
        def getheight(node):
            if not node:
                return 0
            left = getheight(node.left) 
            right = getheight(node.right) 
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return 1+max(left,right)
        ans = getheight(root)
        if ans==-1:
            return False
        else:
            return True


# @lc code=end

