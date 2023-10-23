#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #检查轴对称
        #递归
        def check(node1,node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            if node1.val !=node2.val:
                return False
            return check(node1.left,node2.right) and check(node1.right,node2.left)
        return check(root,root)
        #层次遍历
        # queue  =[root]
        # while(queue):
        #     next_queue = list()
        #     layer = list()
        #     for node in queue:
        #         if not node:
        #             layer.append(None)
        #             continue
        #         next_queue.append(node.left)
        #         next_queue.append(node.right)

        #         layer.append(node.val)
        #     if layer!=layer[::-1]:
        #         return False
        #     queue = next_queue

        # return True
        
        
            
# @lc code=end

