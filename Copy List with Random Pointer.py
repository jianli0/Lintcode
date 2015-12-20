# Definition for singly-linked list with a random pointer.
class RandomListNode:
   def __init__(self, x):
       self.label = x
       self.next = None
       self.random = None

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return None
        self.copyNext(head)
        self.copyRandom(head)
        return self.splitList(head)

    def copyNext(self, head):
        while head is not None:
            newNode = RandomListNode(head.label)
            newNode.random = head.random
            newNode.next = head.next
            head.next = newNode
            head = head.next.next

    def copyRandom(self, head):
        while head is not None:
            if head.next.random is not None:
                head.next.random = head.random.next
            head = head.next.next

    def splitList(self, head):
        newHead = head.next
        while head is not None:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next is not None:
                temp.next = temp.next.next
        return newHead


