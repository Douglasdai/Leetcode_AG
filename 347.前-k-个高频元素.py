#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #使用Counter?
        # from collections import Counter
        # ans = Counter(nums)
        # anss = ans.most_common(k)
        # res =[]
        # for i in range(k):
        #     res.append(anss[i][0])
        # return res
        #正常方法 使用小顶堆
        import heapq
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i],0)+1

        #建堆
        pri_que = []
        for key,val in map_.items():
            heapq.heappush(pri_que,(val,key))
            if len(pri_que)>k:
                heapq.heappop(pri_que)
        #倒序输出
        res = [0]*k
        for i in range(k-1,-1,-1):
            res[i] = heapq.heappop(pri_que)[1]
        return res

# @lc code=end

