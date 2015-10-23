"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        num = 0
        start = head
        while start != None:
            start = start.next
            num += 1
        order = num - n
        print "num % d and order %d" %(num, order)

        num = 0
        dummy = ListNode(0,head)
        start = dummy
        while start != None and num != order:
            start = start.next
            num += 1

        start.next = start.next.next


        return dummy.next

        # write your code here

if __name__ == '__main__':
    b6 = ListNode(2)
    b5 = ListNode(5, b6)
    b4 = ListNode(2, b5)
    b3 = ListNode(3, b4)
    b2 = ListNode(4, b3)
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

    start = a.removeNthFromEnd(b1, 6)
    while start != None:
        print start.val
        start = start.next


