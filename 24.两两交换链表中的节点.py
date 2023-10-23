#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #只能节点交换
        #正常模拟
        d_head = ListNode(next = head)
        current = d_head
        #下两个有才行
        #迭代法+画图
        while current.next and current.next.next:
            #1234

            temp = current.next
            temp1  =current.next.next.next

            current.next = current.next.next
            current.next.next = temp
            temp.next = temp1
            current = current.next.next
        
        return d_head.next
    


# @lc code=end

