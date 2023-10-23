#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
import collections
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #很难
        #深信服 面试题
        #滑动窗口问题
        if len(t)>len(s):
            return ""
        need=collections.defaultdict(int)
        needCnt =len(t)
        for c in t:
            need[c]+=1
        i=0
        res = (0,float('inf'))
        for j,c in enumerate(s):
            if need[c]>0:
                needCnt-=1
            need[c]-=1
            #包含了所有的
            if needCnt==0:
                while True:
                    c = s[i]
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i<res[1]-res[0]:
                    res=(i,j)
                need[s[i]]+=1
                needCnt+=1
                i+=1
        return "" if res[1]>len(s) else s[res[0]:res[1]+1]
        



# @lc code=end

