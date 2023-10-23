#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #中序遍历
        # res = []
        # def dfs(node):
        #     if not node:
        #         return 
        #     dfs(node.left)
        #     res.append(node.val)
        #     dfs(node.right)
        
        # dfs(root)
        # return res

        #迭代法
        if not root:
            return []
        stack =[]
        res = []
        cur = root
        while cur or stack:
            #访问最左边
            if cur:
                stack.append(cur)
                cur =cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res



# @lc code=end

