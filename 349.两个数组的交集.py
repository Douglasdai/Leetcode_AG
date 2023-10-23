#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # from collections import Counter
        n1 = set(nums1)
        n2 = set(nums2)
        return list(n1 &n2)




# @lc code=end

