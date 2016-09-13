class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if lists:
            if len(lists) == 1:
                return lists[0]
            else:
                merged = self.merge(lists[0], lists[1])
                if len(lists) == 2:
                    return merged
                else:
                    for i in range(2, len(lists)):
                        merged = self.merge(merged,lists[i])
                    return merged


    def merge(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy

        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail= tail.next
        if head1 is not None:
            tail.next = head1
        else:
            tail.next = head2
        return dummy.next


if __name__ == '__main__':
    b6 = ListNode(12)
    b5 = ListNode(10, b6)
    b4 = ListNode(8, b5)
    b3 = ListNode(5, b4)
    b2 = ListNode(4, b3)
    b1 = ListNode(1, b2)

    a3 = ListNode(7)
    a2 = ListNode(6, a3)
    a1 = ListNode(5, a2)


    a = Solution()
    start = a.mergeKLists([b1,a1])

    while start != None:
        print start.val
        start = start.next

