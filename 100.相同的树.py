#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #树遍历 查看是相同
        if p is None and q is None:
            return True
        if (p is None and q is not None)or(p is not  None and q is None) :
            return False
        if p.val !=q.val:
            return False
        res1 ,res2 =[],[]
        def dfs(node,res):
            if not node:
                res.append(100000)
                return 
            res.append(node.val)
            dfs(node.left,res)
            dfs(node.right,res)
        dfs(p,res1)
        dfs(q,res2)
        if len(res1)!=len(res2):
            return False
        for i in range(len(res1)):
            if res1[i]!=res2[i]:
                return False
        return True

# @lc code=end

