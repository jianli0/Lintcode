# Recursion
"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        preorder = []
        stack = []

        if root == None:
            return preorder

        stack.append(root)

        while len(stack):
            node = stack.pop()
            preorder.append(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)

        return preorder

if __name__ == '__main__':
    a = Solution()

    a1 = TreeNode(123)
    a2 = TreeNode(342)
    a3 = TreeNode(3)
    a4 = TreeNode(9)
    a5 = TreeNode(6)

    a1.left = a2
    a1.right = a4
    a2.left = a3
    a3.right = a5

    aa1 = TreeNode(1)
    aa2 = TreeNode(2)
    aa3 = TreeNode(3)
    aa4 = TreeNode(4)
    aa5 = TreeNode(5)

    aa1.left = aa2
    aa1.right = aa3
    aa3.left = aa4
    aa3.right = aa5

    print a.preorderTraversal(a1)
    print a.preorderTraversal(None)
    print a.preorderTraversal(aa1)
