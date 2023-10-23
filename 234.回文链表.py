#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #快慢指针
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result    

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

  
        #迭代反转
        cur = None
        pre = head
        h2 = copy.deepcopy(head) 
        cnt =0
        while pre is not None:
            t =pre.next
            pre.next = cur 
            cur = pre
            pre = t
            cnt+=1
        # print(cnt)
        # cnt=0
        while h2 is not None:
            if h2.val!=cur.val:
                return False
            # cnt+=1
            # print(h2.val,cur.val)
            h2 = h2.next
            cur = cur.next
            # cnt-=1
        # print(cnt)
        return True

# @lc code=end

