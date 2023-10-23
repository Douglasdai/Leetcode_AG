#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        #集合的思想
        mem = set()
        while n!=1:
            n = sum([int(i)**2 for i in str(n)])
            if n in mem:return False
            else:mem.add(n)
        else:
            return True

        #迭代 快慢指针思想
        


# @lc code=end

