#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from collections import deque
class MyQueue:
    def __init__(self) -> None:
        self.queue = deque()
    #每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    #同时pop之前判断队列当前是否为空。
    def pop(self,value):
        if self.queue and value ==self.queue[0]:
            self.queue.popleft()

    #如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    #这样就保持了队列里的数值是单调从大到小的了。
    def push(self,value):
        while self.queue and value>self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
    
    def front(self):
        return self.queue[0]

# @lc code=start
class Solution:
    #制作单调队列
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # from collections import deque
        # q = deque() # stores *indices*
        # res = []
        # for i, cur in enumerate(nums):
        #     while q and nums[q[-1]] <= cur:
        #         q.pop()
        #     q.append(i)
        #     # remove first element if it's outside the window
        #     if q[0] == i - k:
        #         q.popleft()
        #     # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
        #     if i >= k - 1:
        #         res.append(nums[q[0]])
        # return res
        
        #单调队列 题解
        from collections import deque
        #存的是下标
        q = deque()
        for i in range(k):
            while q and nums[i]>=nums[q[-1]]:
                q.pop()
            q.append(i)
        
        ans = [nums[q[0]]]
        for i in range(k,len(nums)):
            while q and nums[i]>=nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0]<=i-k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans
# @lc code=end

