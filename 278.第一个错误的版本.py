#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    ...
class Solution:
    def firstBadVersion(self, n: int) -> int:
        #二分查找
        l,r = 1,n
        while l<r:
            mid  = l+(r-l)//2
            #在mid里mian
            if isBadVersion(mid):
                r = mid
            else:
                l = mid+1
        return l

        
# @lc code=end

