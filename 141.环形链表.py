#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if head.next is None:
            return False
        #开始遍历
        while head.next is not None:
            if head.val ==100001:
                return True
            else:
                head.val =100001
                head = head.next
        return False

        #循环快慢指针
        try:
            slow =head
            fast  =head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


            
        
# @lc code=end

