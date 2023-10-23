#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow,fast = head,head
        cnt=0
        for i in range(n):
            fast = fast.next
            cnt+=1
        #应对[1]的情况
        if not fast:return head.next
        #到prev
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        #找到了slow的节点
        slow.next = slow.next.next
        return head


# @lc code=end

