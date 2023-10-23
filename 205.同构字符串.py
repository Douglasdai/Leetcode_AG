#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #双射所以要两个
        # s2t, t2s = {}, {}
        # for i in range(len(s)):
        #     if s[i] in s2t and s2t[s[i]] != t[i]:
        #         return False
        #     if t[i] in t2s and t2s[t[i]] != s[i]:
        #         return False
        #     s2t[s[i]] = t[i]
        #     t2s[t[i]] = s[i]
        # return True
        #满足双射关系即可
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
# @lc code=end

