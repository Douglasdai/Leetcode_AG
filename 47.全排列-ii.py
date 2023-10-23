#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #全排列去重
        #可以先全排然后去重
        def dfs(nums,path,res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
        res = []
        dfs(nums,[],res)
        res2 = list(set(map(tuple,res)))
        return res2
    #方法2 
    #添加限制条件，排序
    def permuteUnique2(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

# @lc code=end

