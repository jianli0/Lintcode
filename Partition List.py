'''
Definition of ListNode
'''

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode
    """
    def partition(self, head, x):
        # write your code here
        if head is None:
            return None

        leftDummy = ListNode(0)
        rightDummy = ListNode(0)
        left, right = leftDummy, rightDummy

        while not head is None:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next

        right.next = None
        left.next = rightDummy.next
        return leftDummy.next

if __name__ == '__main__':
    b6 = ListNode(2)
    b5 = ListNode(5, b6)
    b4 = ListNode(2, b5)
    b3 = ListNode(3, b4)
    b2 = ListNode(4, b3)
    b1 = ListNode(1, b2)


    a = Solution()
    start = a.partition(b1, 3)

    while start != None:
        print start.val
        start = start.next

