# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        while head.next != None:
            #debuging
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return dummy.next
        # Write your code here

if __name__ == '__main__':
    a1 = ListNode(1)
    a2 = ListNode(1)
    a1.next = a2
    a = Solution()
    newLinkedList = a.removeElements(a1,1)

    while newLinkedList != None:
        print newLinkedList.val,
        newLinkedList = newLinkedList.next
