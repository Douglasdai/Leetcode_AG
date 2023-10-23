#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
from operator import add,sub,mul
class Solution:
    #使用字典
    op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x / y)}
    
    def evalRPN(self, tokens: List[str]) -> int:
        #模拟
        stack =[]
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                if token=='/':
                    ans = int(stack[-2]/stack[-1])
                elif token=='+':
                    ans = stack[-2]+stack[-1]
                elif token=='-':
                    ans = stack[-2]-stack[-1]
                else:
                    #×
                    ans = stack[-2]*stack[-1]
                stack.pop()
                stack.pop()
                stack.append(ans)
        return stack[0]
    
    def evalRPN2(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1,op2))
        return stack.pop()
# @lc code=end

