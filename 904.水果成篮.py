#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#
import collections
# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #滑动窗口
        ans = 0
        count  =collections.defaultdict(int)
        l =0
        for r,t in enumerate(fruits):
            count[t]+=1
            while len(count)>2:
                count[fruits[l]]-=1
                if count[fruits[l]]==0:
                    del count[fruits[l]]
                l+=1
            ans = max(ans,r-l+1)
        return ans
            
            

# @lc code=end

