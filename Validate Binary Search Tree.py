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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        preorder = self.inorderTraversal(root)
        original = preorder[:]
        preorder = list(set(preorder))
        preorder.sort()

        # debug
        # print original
        # print "-"*30
        # print preorder

        return (original == preorder)

    def inorderTraversal(self, root):
        # leaf or None
        result = []
        if root == None:
            return result

        # Divide
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        # Conquer
        result = result + left
        result.append(root.val)
        result = result + right

        return result

if __name__ == '__main__':
    a = Solution()

    a1 = TreeNode(9)
    a2 = TreeNode(6)
    a3 = TreeNode(12)
    a4 = TreeNode(5)
    a5 = TreeNode(8)
    a6 = TreeNode(11)
    a7 = TreeNode(13)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a3.left = a6
    a3.right = a7

    aa1 = TreeNode(1)
    aa2 = TreeNode(2)
    aa3 = TreeNode(3)
    aa4 = TreeNode(4)
    aa5 = TreeNode(5)

    aa1.left = aa2
    aa1.right = aa3
    aa3.left = aa4
    aa3.right = aa5

    print a.isValidBST(a1)
    print a.isValidBST(None)
    print a.isValidBST(aa1)
