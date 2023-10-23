#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start

class MyQueue:

    def __init__(self):
        #两个list 实现
        self.stin = []
        self.stout = []


    def push(self, x: int) -> None:
        self.stin.append(x)


    def pop(self) -> int:
        if self.empty():
            return None
        if self.stout:
            return self.stout.pop()
        else:
            for i in range(len(self.stin)):
                self.stout.append(self.stin.pop())
            return self.stout.pop()

    def peek(self) -> int:
        ans = self.pop()
        self.stout.append(ans)
        return ans


    def empty(self) -> bool:
        return not (self.stout or self.stin)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

