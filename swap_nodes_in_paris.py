# https://leetcode.com/problems/swap-nodes-in-pairs/

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        first = head
        second = head.next

        tail = head.next.next

        second.next = first
        first.next = self.swapPairs(tail)

        return second
