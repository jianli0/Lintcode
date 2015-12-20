"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def removeDuplicates(self, head):
        visited = set()
        dummy = ListNode(0,head)
        head = dummy
        while head.next is not None:
            if head.next.val in visited:
                head.next = head.next.next
            else:
                visited.add(head.next.val)
                head = head.next
        return dummy.next


if __name__ == '__main__':
    b6 = ListNode(2)
    b5 = ListNode(5, b6)
    b4 = ListNode(3, b5)
    b3 = ListNode(3, b4)
    b2 = ListNode(2, b3)
    b1 = ListNode(1, b2)


    a = Solution()
    start = a.removeDuplicates(b1)

    while start != None:
        print start.val
        start = start.next

