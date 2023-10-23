#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []
        self.path =[]
    def combine(self, n: int, k: int) -> List[List[int]]:
        #回溯
        self.backtrace2(n,k,1)
        return self.res
    
    def backtrace2(self,n,k,startidx):
        if len(self.path)==k:
            #添加列表的时候放入全部[:]
            self.res.append(self.path[:])
            return 
        for i in range(startidx,n-(k-len(self.path))+2):
            self.path.append(i)
            self.backtrace(n,k,i+1)
            self.path.pop()
        

    def backtrace(self,n,k,startidx):
        if len(self.path)==k:
            #添加列表的时候放入全部[:]
            self.res.append(self.path[:])
            return 
        for i in range(startidx,n+1):
            self.path.append(i)
            self.backtrace(n,k,i+1)
            self.path.pop()

        # # @lc code=end

