#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        #bin 然后倒转
        return int(bin(n)[2:].rjust(32, '0')[::-1], base=2)



        
# @lc code=end

