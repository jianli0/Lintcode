"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Solution provided by Jiuzhang

class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if root is None:
            return node

        curt = root
        while curt != node:
            if node.val < curt.val:
                if curt.left is None:
                    curt.left = node
                curt = curt.left
            else:
                if curt.right is None:
                    curt.right = node
                curt = curt.right
        return root

    def printBinaryTree(self, root):
            if root == None:
                return
            else:
                print root.val,
                self.printBinaryTree(root.left)
                self.printBinaryTree(root.right)

'''
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        if root == None:
            return node

        curt = root

        if node.val < curt.val:
            if curt.left == None:
                curt.left == node
                return root
            else:
                self.insertNode(curt.left, node)
        elif node.val > curt.val:
            if curt.right == None:
                curt.right == node
                return root
            else:
                self.insertNode(curt.right, node)

        # write your code here

    # for test
    def printBinaryTree(self, root):
        if root == None:
            return
        else:
            print root.val,
            self.printBinaryTree(root.left)
            self.printBinaryTree(root.right)
'''

if __name__ == '__main__':
    a = Solution()

    a6 = TreeNode(6)
# Tree 1
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(4)
    a5 = TreeNode(5)

    a3.left = a2
    a3.right = a5
    a2.left = a1
    a5.left= a4

# Tree 2
    b1 = TreeNode(2)
    b2 = TreeNode(1)
    b3 = TreeNode(4)
    b4 = TreeNode(3)

    b1.left = b2
    b1.right = b3
    b3.left = b4

    a.insertNode(a3, a6)
    a.printBinaryTree(a3)

    # a.insertNode(b1, a6)
    # a.printBinaryTree(b1)
