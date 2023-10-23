#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #从后往前走
        s,t  =list(s),list(t)
        i,j = len(s)-1,len(t)-1
        skips = 0
        skipt=0
        while i>=0 or j>=0:
            while i>=0:
                if s[i]=='#':
                    skips+=1
                    i-=1
                elif skips>0:
                    skips-=1
                    i-=1
                else:
                    break
            while j>=0:
                if t[j]=="#":
                    skipt+=1
                    j-=1
                elif skipt>0:
                    skipt-=1
                    j-=1
                else:
                    break
            if i>=0 and j>=0 and s[i]!=t[j]:
                return False
            if (i>=0)!=(j>=0):
                return False
            i-=1
            j-=1
        return True

# @lc code=end

