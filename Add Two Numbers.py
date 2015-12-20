# Definition for singly-linked list.

class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param l1.val: the first list
    # @param l2.val: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 is not None and l2 is not None:
            tail.next = ListNode((l1.val + l2.val + carry) % 10)
            tail = tail.next
            carry = (l1.val + l2.val + carry) / 10
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            tail.next = ListNode((l1.val + carry) % 10)
            tail = tail.next
            carry = (l1.val + carry) / 10
            l1 = l1.next

        while l2 is not None:
            tail.next = ListNode((l2.val + carry) % 10)
            tail = tail.next
            carry = (l2.val + carry) / 10
            l2 = l2.next

        while carry != 0:
            tail.next = ListNode(carry % 10)
            tail = tail.next
            carry = carry / 10

        return dummy.next

if __name__ == '__main__':
    b6 = ListNode(2)
    b5 = ListNode(5)
    b4 = ListNode(2)
    b3 = ListNode(3)
    b2 = ListNode(4)
    b1 = ListNode(1)

    b1.next = b2
    b2.next = b3
    b3.next = b4
    b4.next = b5
    b5.next = b6

    a3 = ListNode(3)
    a2 = ListNode(4)
    a1 = ListNode(1)

    a1.next = a2
    a2.next = a3

    a = Solution()
    start = a.addLists(b1 , a1)

    while start != None:
        print start.val
        start = start.next

