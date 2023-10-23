#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        #dict 解决
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num]+=1
        for di in d.items():
            if di[1]==1:
                return di[0]
            
        #异或解决 高啊
        # a=0 
        # for num in nums:
        #     a = a^num
        # return a 

         

# @lc code=end

