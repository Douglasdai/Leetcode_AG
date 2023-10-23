#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travel(self,cur,path,result):
        path.append(cur.val)
        if not cur.left and not cur.right:
            sPath = '->'.join(map(str,path))
            result.append(sPath)
            return 
        if cur.left:
            self.travel(cur.left,path,result)
            path.pop()
        if cur.right:
            self.travel(cur.right,path,result)
            path.pop()
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #递归+回溯
        res = []
        path = []
        if not root:
            return res 
        self.travel(root,path,res)
        return res
        
        
        
        
        #遍历
        # dfs + stack
    #     if not root:
    #         return []
    #     res, stack = [], [(root, "")]
    #     while stack:
    #         node, ls = stack.pop()
    #         if not node.left and not node.right:
    #             res.append(ls+str(node.val))
    #         if node.right:
    #             stack.append((node.right, ls+str(node.val)+"->"))
    #         if node.left:
    #             stack.append((node.left, ls+str(node.val)+"->"))
    #     return res
        
    # # bfs + queue
    # def binaryTreePaths2(self, root):
    #     if not root:
    #         return []
    #     res, queue = [], collections.deque([(root, "")])
    #     while queue:
    #         node, ls = queue.popleft()
    #         if not node.left and not node.right:
    #             res.append(ls+str(node.val))
    #         if node.left:
    #             queue.append((node.left, ls+str(node.val)+"->"))
    #         if node.right:
    #             queue.append((node.right, ls+str(node.val)+"->"))
    #     return res
        
    # # dfs recursively
    # def binaryTreePaths3(self, root):
    #     if not root:
    #         return []
    #     res = []
    #     self.dfs(root, "", res)
    #     return res
    
    # def dfs(self, root, ls, res):
    #     if not root.left and not root.right:
    #         res.append(ls+str(root.val))
    #     if root.left:
    #         self.dfs(root.left, ls+str(root.val)+"->", res)
    #     if root.right:
    #         self.dfs(root.right, ls+str(root.val)+"->", res)
			
    # def binaryTreePaths1(self, root):
    #     return self.dfs(root, "")
    
    # def dfs(self, root, path):
    #     if not root:
    #         return []
    #     path += str(root.val)
    #     if not root.left and not root.right:
    #         return [path]
    #     path += "->"
    #     return self.dfs(root.left, path) + self.dfs(root.right, path)
    
    # def binaryTreePaths(self, root): # inorder
    #     stack, ret = [(root, "")], []
    #     while stack:
    #         node, path = stack.pop()
    #         if node:
    #             if not node.left and not node.right:
    #                 ret.append(path+str(node.val))
    #             s = path + str(node.val) + "->"
    #             stack.append((node.right, s))
    #             stack.append((node.left, s))    
    #     return ret
# @lc code=end

