"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        if head is None or head.next is None:
            return
        middle = self.findMiddle(head)
        print "middle.val is %d"%middle.val
        tail = self.reverseList(middle.next)
        middle.next = None

        #  debug
        #  start = tail
        #  while start!= None:
            #  print start.val
            #  start = start.next

        return self.merge(head, tail)

    def findMiddle(self , head):
        if head is not None:
            slow = head
            fast = head.next
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            # debug
            #  print " middle value is %d" % slow.val
            return slow


    def reverseList(self, head):
        newHead = None
        while head is not None:
            tmp = head.next
            head.next = newHead
            newHead = head
            head = tmp
        return newHead

    def merge(self,head1,head2):
        index = 0
        dummy = ListNode(0)
        start = dummy

        print "head1"
        start = head1
        while start != None:
            print start.val
            start = start.next

        print "head2"
        start = head2
        while start != None:
            print start.val
            start = start.next

        while head1 is not None and head2 is not None:
            if index % 2 == 0:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next
            index += 1
        if head1 is not None:
            dummy.next = head1
        else:
            dummy.next = head2

        #  return start.next


if __name__ == '__main__':
    b6 = ListNode(6)
    b5 = ListNode(5, b6)
    b4 = ListNode(4, b5)
    b3 = ListNode(3, b4)
    b2 = ListNode(2, b3)
    b1 = ListNode(1, b2)

    a2 = ListNode(-1)
    a1 = ListNode(1, a2)

    a = Solution()

    start = a.reorderList(a1)
    #  debug
    print "hello world"
    while start != None:
        print start.val
        start = start.next

