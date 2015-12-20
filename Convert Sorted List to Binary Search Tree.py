"""
Definition of ListNode
Definition of TreeNode:
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        if head is None:
            return None
        pre, middle = self.findMiddle(head)
        treenode = TreeNode(middle.val)
        rightList = middle.next
        if pre:
            leftList = head
            pre.next = None
        else:
            leftList = None

        treenode.left = self.sortedListToBST(leftList)
        treenode.right= self.sortedListToBST(rightList)
        return treenode

    def findMiddle(self,head):
        if head is None:
            return
        pre = None
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        return pre, slow


def printTree(node):
    if node is None:
        return
    else:
        printTree(node.left)
        print node.val
        printTree(node.right)


if __name__ == '__main__':
    # test list
    b7 = ListNode(7)
    b6 = ListNode(6, b7)
    b5 = ListNode(5, b6)
    b4 = ListNode(4, b5)
    b3 = ListNode(3, b4)
    b2 = ListNode(2, b3)
    b1 = ListNode(1, b2)

    # test
    #  a1 = TreeNode(1)
    #  a2 = TreeNode(2)
    #  a3 = TreeNode(3)
    #  a2.left = a1
    #  a2.right= a3

    a = Solution()

    root = a.sortedListToBST(b1)
    printTree(root)


