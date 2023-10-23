#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        #可以正常按找层次遍历，然后倒转列表
        #层次
        # res = []
        # levels = []
        # def helper(node,level,levels):
        #     if not node:
        #         return 
        #     if len(levels)==level:
        #         levels.append([])
        #     levels[level].append(node.val)
        #     helper(node.left,level+1,levels)
        #     helper(node.right,level+1,levels)
        # helper(root,0,levels)
        # levels =levels[::-1]
        # return levels
        #直接

# @lc code=end

