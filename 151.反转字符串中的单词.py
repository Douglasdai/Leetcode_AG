#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(" ")[::-1]
        a = " ".join(ss).split()
        return " ".join(a)

    def reverseWords2(self, s: str) -> str:
        # 将字符串拆分为单词，即转换成列表类型
        words = s.split()

        # 反转单词
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # 将列表转换成字符串
        return " ".join(words)

# @lc code=end
# s = "a good   example"
# ss = s.split(" ")[::-1]
# a = " ".join(ss).split()
# print(" ".join(a))
