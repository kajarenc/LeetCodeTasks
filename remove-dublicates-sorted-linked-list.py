# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)

        result = dummyHead
        current = head

        while current:
            val = current.val
            new_node = ListNode(val)
            result.next = new_node
            result = result.next

            while current.next and current.next.val == val:
                current = current.next
            current = current.next

        return dummyHead.next
