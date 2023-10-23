#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #回溯算法
        def dfs(nums,path,res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
        res = []
        dfs(nums,[],res)
        return res
# @lc code=end

