#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #使用两次二分法,找左边界和右边界
        l,r=0,len(nums)-1
        ansleft,ansright =-1,-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                ansleft = mid
                r = mid-1
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        l,r= 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                ansright = mid
                l = mid+1
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return [ansleft,ansright]
        
# @lc code=end

