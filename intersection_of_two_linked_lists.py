# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Solution from here: https://www.youtube.com/watch?v=IpBfg9d4dmQ

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        first_ptr = headA
        second_ptr = headB

        while first_ptr != second_ptr:

            if first_ptr is None:
                first_ptr = headB
            else:
                first_ptr = first_ptr.next

            if second_ptr is None:
                second_ptr = headA
            else:
                second_ptr = second_ptr.next

        return first_ptr

