#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # c = bin(a)+bin(b)
        # return c
        # 模拟
        return '{0:b}'.format(int(a, 2) + int(b, 2))
# @lc code=end

