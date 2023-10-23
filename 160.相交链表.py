#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #双指针
        #走对方的路
        # if headA is None or headB is None:
        #    return None
        # A, B = headA, headB
        # while A != B:
        #     A = A.next if A else headB
        #     B = B.next if B else headA
        # return A
        
        #双指针 进行位移
        cnta,cntb = 0,0
        A,B = headA,headB
        while A is not None:
            A = A.next
            cnta+=1
        while B is not None:
            B = B.next
            cntb+=1
        if cnta<cntb:
            for i in range(cntb-cnta):
                headB = headB.next
        else:
            for i in range(cnta-cntb):
                headA = headA.next
        #开始遍历
        while headA or headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None


        
# @lc code=end

