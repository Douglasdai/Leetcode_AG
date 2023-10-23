#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #二分
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r =mid-1
            #找到了就return mid
            else:
                return mid
        #没有找到
        #返回最右+1 个
        return r+1

        

# @lc code=end

