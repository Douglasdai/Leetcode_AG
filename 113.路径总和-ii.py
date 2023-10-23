#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        #递归去寻找有无路径
        # if not root:
        #     return 
        res = []
        path =[]
        def trvael(node,target,path,res):
            if not node:
                return 
            path.append(node.val)
            target-=node.val
            if not node.left and not node.right and target ==0:
                res.append(list(path))
            trvael(node.left,target,path,res)
            trvael(node.right,target,path,res)
            path.pop()
        trvael(root,targetSum,path,res)
        return res
# @lc code=end

