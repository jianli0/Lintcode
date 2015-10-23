"""
Definition of ListNode
"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        dummy = ListNode(None, head)
        head = dummy

        while head.next and head.next.next:
            if head.next.val == head.next.next.val:
                val = head.next.val
                while head.next is not None and head.next.val == val:
                    head.next = head.next.next
            else:
                head = head.next

        return dummy.next




if __name__ == '__main__':
    b6 = ListNode(4)
    b5 = ListNode(2, b6)
    b4 = ListNode(2, b5)
    b3 = ListNode(1, b4)
    b2 = ListNode(1, b3)
    b1 = ListNode(1, b2)


    a = Solution()
    #  start = a.removeNthFromEnd(b1, 2)
    #  while start != None:
        #  print start.val
        #  start = start.next

    #  start = a.removeNthFromEnd(b1, 1)
    #  while start != None:
        #  print start.val
        #  start = start.next

    start = a.deleteDuplicates(b1)
    while start != None:
        print start.val
        start = start.next





