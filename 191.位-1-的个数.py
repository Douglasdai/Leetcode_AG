#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(bin(n))
        ans =0
        print(s)
        for ss in s:
            if ss=='1':
                ans+=1
        return ans
        
# @lc code=end

