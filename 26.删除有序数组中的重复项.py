#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #快慢指针
        # slow,fast = 0,1
        # while fast in range(len(nums)):
        #     if nums[slow]==nums[fast]:
        #         fast+=1
        #     else:
        #         nums[slow+1]=nums[fast]
        #         #不相等了
        #         slow+=1
        #         fast+=1
        # return slow+1
            
        #python特有可以按照set 去做
        # numss = set(nums)
        
        # return len(numss)

    
# @lc code=end

