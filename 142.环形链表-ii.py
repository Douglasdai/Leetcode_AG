#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #快慢指针
        s,f = head,head 
        while f and f.next:
            f = f.next.next
            s = s.next
            #相遇了
            if s==f:
                while f!=head:
                    f = f.next
                    head = head.next
                return head
        return None

# @lc code=end

