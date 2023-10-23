#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def searchBST(self, cur, freq_map):
    #     if cur is None:
    #         return
    #     freq_map[cur.val] += 1  # 统计元素频率
    #     self.searchBST(cur.left, freq_map)
    #     self.searchBST(cur.right, freq_map)

    # def findMode(self, root):
    #     #递归+字典
    #     from collections import defaultdict
    #     freq_map = defaultdict(int)  # key:元素，value:出现频率
    #     result = []
    #     if root is None:
    #         return result
    #     self.searchBST(root, freq_map)
    #     max_freq = max(freq_map.values())
    #     for key, freq in freq_map.items():
    #         if freq == max_freq:
    #             result.append(key)
    #     return result
    
    # 如果中序遍历 ，有序
    def __init__(self):
        self.maxCount = 0  # 最大频率
        self.count = 0  # 统计频率
        self.pre = None
        self.result = []

    def searchBST(self, cur):
        if cur is None:
            return

        self.searchBST(cur.left)  # 左
        # 中
        if self.pre is None:  # 第一个节点
            self.count = 1
        elif self.pre.val == cur.val:  # 与前一个节点数值相同
            self.count += 1
        else:  # 与前一个节点数值不同
            self.count = 1
        self.pre = cur  # 更新上一个节点

        if self.count == self.maxCount:  # 如果与最大值频率相同，放进result中
            self.result.append(cur.val)

        if self.count > self.maxCount:  # 如果计数大于最大值频率
            self.maxCount = self.count  # 更新最大频率
            self.result = [cur.val]  # 很关键的一步，不要忘记清空result，之前result里的元素都失效了

        self.searchBST(cur.right)  # 右
        return

    def findMode(self, root):
        self.count = 0
        self.maxCount = 0
        self.pre = None  # 记录前一个节点
        self.result = []

        self.searchBST(root)
        return self.result

# @lc code=end

