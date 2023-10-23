#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
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
        #递归要用外面的参数
        self.maxeval = float('-inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #递归 验证
        # maxeval = float('-inf')
        # if root is None:return True
        # left = self.isValidBST(root.left)
        # #记录上一个节点
        # #有序无序
        # if self.maxeval < root.val:
        #     self.maxeval = root.val
        # else:
        #     return False
        # right = self.isValidBST(root.right)
        # return left and right
    #可以遍历进入数组来解决，只需要判断有序就行了

    #迭代法 用层次遍历
        stack = []
        cur =root
        pre = None#记录前一个节点
        while cur is not None or len(stack)>0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left #左
            else:
                cur = stack.pop()
                if pre is not None and cur.val<=pre.val:
                    return False#中
                pre =cur
                cur = cur.right#右
        return True


# @lc code=end

