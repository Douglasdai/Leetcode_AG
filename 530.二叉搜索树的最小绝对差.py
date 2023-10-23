#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
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
        self.pre = None
        self.res = float('inf')

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #迭代法看看
        stack = []
        cur = root
        pre = None
        res = float('inf')
        while cur is not None or len(stack)>0:
            if cur is not None:
                #前一个
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre is not None:
                    res = min(cur.val-pre.val,res)
                pre = cur
                cur = cur.right
        return res




    
    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
        #中序遍历 递归
        self.trvael(root)
        return self.res
    
    def trvael(self,root):
        if not root:
            return 
        self.getMinimumDifference(root.left)
        if self.pre is not None :
            self.res = min(root.val-self.pre.val,self.res)
        self.pre = root 
        self.getMinimumDifference(root.right)

# @lc code=end

