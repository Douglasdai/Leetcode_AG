#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #进制转换 A->1
        #需要 先-1才行
        ans = list()
        while columnNumber > 0:
            columnNumber -= 1
            ans.append(chr(columnNumber % 26 + ord("A")))
            columnNumber //= 26
        return "".join(ans[::-1])



# @lc code=end

