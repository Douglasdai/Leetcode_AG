#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, x: int) -> bool:
        if x <= 1:
            return True
        l,r = 0,x-1
        while l<=r:
            mid = (l+r)//2
            if mid*mid ==x:
                return True
            elif mid*mid >x:
                r = mid-1
            else:
                l = mid+1
        return False
# @lc code=end

