#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        #数学问题
        #斐波那契数列
        # s = [1,2]
        # if n<=2:
        #     return s[n-1]
        # while (len(s)<n):
        #     s.append(s[-1]+s[-2])
        # return s[n-1]
        #动态规划 dp
        #空间比较大
        
        dp  = [0]*(n+1)
        dp[0] = dp[1]=1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]
# @lc code=end

