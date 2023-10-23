#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #方法1 遍历
        #双指针
        slow ,fast = 0,1
        #slow定位0
        #fast 定位非0
        for fast in range(len(nums)):
            if nums[slow]==0 and nums[fast]!=0:
               nums[slow],nums[fast] = nums[fast],nums[slow]
               slow+=1
               fast+=1
            #    swap(nums[slow],nums[fast])
            elif nums[slow]!=0:
               slow+=1
            elif nums[fast]==0:
               fast+=1
        

# 0,1,0,3,9
# 1,0 0 3,9
#   slow  fast 
#   3, 0 0 9
#      slow      

# @lc code=end

