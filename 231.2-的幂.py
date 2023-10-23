#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1 or n==2:return True
        if n==0:return False
        while n>2:
            n/=2
        if n==0 or n==2:
            return True
        else:return False

# @lc code=end

