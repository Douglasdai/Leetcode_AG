#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
    #     #回溯
        
        res = []    
        self.backtrace(k,1,[],res,0,n)
        return res
    
    def backtrace(self,k,startidx,path,res,sumn,n):
        if sumn>n:
            return 
        if len(path)==k:
            if sumn==n:
                res.append(path[:])
            return 
        for i in range(startidx,9-(k-len(path))+2):
            sumn+=i
            path.append(i)
            self.backtrace(k,i+1,path,res,sumn,n)
            sumn-=i
            path.pop()
        

# @lc code=end

