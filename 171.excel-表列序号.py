#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col = len(columnTitle)
        ans =0
        for s in columnTitle:
            ans+=(ord(s)-64)*(26**(col-1))
            col-=1
        
        return ans

# @lc code=end

