#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #递归
        if head is None or head.next is None:
            return head
        ret = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return ret
        
        #迭代
        # cur = None
        # prev = head
        # while(prev!=None):
        #     t = prev.next
        #     prev.next = cur
        #     cur=prev 
        #     prev =t
        # return cur
        #替换值
        # if not head:
        #     return head
        # ans = [0]
        # a,b = head,head
        # while a is not None:
        #     ans.append(a.val)
        #     a = a.next
        # ans = ans[::-1]
        # cnt=0
        # while b is not None:
        #     b.val = ans[cnt]
        #     b = b.next
        #     cnt+=1
        # return head

# @lc code=end

