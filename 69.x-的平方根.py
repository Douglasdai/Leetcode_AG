#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        #模拟
        # c = math.sqrt(x)
        # return int(c)
        #二分查找
        # x = 0 或 1 时，直接返回结果
        if x <= 1:
            return x
        l,r = 0,x-1
        while l<=r:
            mid = (l+r)//2
            if mid*mid ==x:
                return mid
            elif mid*mid >x:
                r = mid-1
            else:
                l = mid+1
        return r


        # left, right = 1, x
        # while left <= right:
        #     middle = left + (right - left) // 2
        #     if middle ** 2 == x:
        #         return middle
        #     elif middle ** 2 > x:
        #         right = middle - 1
        #     else:
        #         left = middle + 1
        
        # return right
# @lc code=end

