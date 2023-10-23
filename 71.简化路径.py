#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories =path.split('/')
        for dir in directories:
            if dir =='.' or not dir:
                continue
            elif dir=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return '/'+'.'.join(stack)


# @lc code=end

