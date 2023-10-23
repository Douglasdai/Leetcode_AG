#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        #移动匹配 
        #掐头去尾找自己
        # ss = s+s
        # ss = ss[1:-1]
        # if s in ss:
        #     return True
        # return False
        #KMP算法解决
        def getNext(next,s):
            next[0] =-1
            j =-1 
            for i in range(1,len(s)):
                while j>=0 and s[i]!=s[j+1]:
                    j = next[j]
                if s[i]==s[j+1]:
                    j+=1
                next[i] = j
            return next
        if len(s)==0:
            return False
        next = [0]*len(s)
        j=-1
        getNext(next,s)
        if next[-1]!=-1 and len(s) % (len(s)-(next[-1]+1))==0:
            return True
        return False
                

# @lc code=end

