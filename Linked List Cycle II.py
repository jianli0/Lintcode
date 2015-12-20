"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: The node where the cycle begins.
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        first = head
        second = head

        while first and second:
            first = first.next
            second = second.next
            if second is not None:
                second = second.next
            if first == second:
                break

        if second is None:
            return None

        first = head
        while first != second:
            first = first.next
            second = second.next

        return second
