#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #python一行解决
        # return sorted([num*num for num in nums])
        #双指针办法
        #非递减的
        #最大的数一定在两边，所以用双指针从两边开始遍历，将更大的放到新数组的最后
        s,f=0,len(nums)-1
        ans = [0]*len(nums)
        i =len(nums)
        while s<=f:
            i-=1
            if nums[s]+nums[f]<0:
                ans[i] = nums[s]*nums[s]
                s+=1
            else:
                ans[i] = nums[f]*nums[f]
                f-=1
        return ans
        



# @lc code=end

