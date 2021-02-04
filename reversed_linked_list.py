class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#IMPERATIVE

class SolutionIterative:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        new_head = head
        prev = None

        while new_head:
            next_node = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = next_node
        return prev


# RECURISIVE

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(head):
            if head is None or head.next is None:
                tail = head
                return head, tail

            new_head, tail = reverse(head.next)
            tail.next = head
            head.next = None

            return new_head, tail.next

        head, tail = reverse(head)
        return head


# MORE SHORT RECURSIVE SOLUTION

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        second = head.next
        new_head = self.reverseList(second)
        head.next.next = head
        head.next = None
        return new_head