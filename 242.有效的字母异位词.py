#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #字典解决
        # ss,tt = [0]*27,[0]*27
        # for a in s:
        #     ss[ord(a)-97] +=1
        # for b in t:
        #     tt[ord(b)-97] +=1    
        # for x,y in zip(ss,tt):
        #     if x!=y:
        #         return False
        # return True
        #单列表解决
        # if len(s) != len(t):
        #     return False
        
        # freq = [0] * 26
        # for i in range(len(s)):
        #     freq[ord(s[i]) - ord('a')] += 1
        #     freq[ord(t[i]) - ord('a')] -= 1
        
        # for i in range(len(freq)):
        #     if freq[i] != 0:
        #         return False
        
        # return True
    
        #counter 解决
        from collections import Counter
        s_ = Counter(s)
        t_ =Counter(t)
        return  s_==t_
# @lc code=end

