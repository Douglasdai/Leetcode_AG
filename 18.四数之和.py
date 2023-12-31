#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i]>target and nums[i]>0 and target>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left,right = j+1,n-1
                while left<right:
                    s = nums[i]+nums[j]+nums[left]+nums[right]
                    if s<target:
                        left+=1
                    elif s>target:
                        right-=1
                    else:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        #去重
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
        return res
# @lc code=end

