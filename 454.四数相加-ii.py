#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        #使用dict 来解决
        N1 = dict()
        
        for n1 in nums1:
            for n2 in nums2:
                N1[n1+n2] = N1.get(n1+n2,0)+1
        cnt = 0
        for n3 in nums3:
            for n4 in nums4:
                key = -n3-n4
                if key in N1:
                    cnt+=N1[key]
        return cnt

# @lc code=end

