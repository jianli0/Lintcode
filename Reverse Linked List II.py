"""
Definition of ListNode

"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if m >= n or head is None:
            return head

        dummy = ListNode(0, head)
        head = dummy

        for i in range(1,m):
            if head is None:
                return
            head = head.next

        preNode = head
        mNode = head.next
        nNode = mNode
        postNode = mNode.next

        num = 1
        rvsRange = n - m
        curt = None




            num += 1





if __name__ == '__main__':
    b6 = ListNode(2)
    b5 = ListNode(5, b6)
    b4 = ListNode(2, b5)
    b3 = ListNode(3, b4)
    b2 = ListNode(4, b3)
    b1 = ListNode(1, b2)


    a = Solution()
    start = a.sortList(b1)

    while start != None:
        print start.val
        start = start.next

