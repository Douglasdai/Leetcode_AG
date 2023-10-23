#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #字典
        #其实可以用Counter 中 subtract
        from collections import Counter
        maga =Counter(magazine)
        for ran in ransomNote:
            if ran in maga:
                maga[ran]-=1
            else:
                return False
        for m in maga:
            if maga[m]<0:
                return False
        return True
# @lc code=end

