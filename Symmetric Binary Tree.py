"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param root, the root of binary tree.
    @return true if it is a mirror of itself, or false.
    """
    def isSymmetric(self, root):
        # Write your code here
        return self.leftFirst(root,0) == self.rightFirst(root,0)

    def leftFirst(self,root,depth):
        res = []
        if root == None:
            res.append(["*",depth])
            return res

        left = self.leftFirst(root.left,depth + 1)
        right = self.leftFirst(root.right,depth + 1)

        res = res + left
        res.append([root.val,depth])
        res = res + right
        return res

    def rightFirst(self,root,depth):
        res = []
        if root == None:
            res.append(["*",depth])
            return res

        left = self.rightFirst(root.left,depth + 1)
        right = self.rightFirst(root.right,depth + 1)

        res = res + right
        res.append([root.val,depth])
        res = res + left
        return res

if __name__ == '__main__':
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(2)
    a4 = TreeNode(3)
    a5 = TreeNode(4)
    a6 = TreeNode(4)
    a7 = TreeNode(3)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a3.left = a6
    a3.right = a7


    b1 = TreeNode(1)
    b2 = TreeNode(1)
    b1.right = b2

    a = Solution()
    print a.isSymmetric(a1)
    print "#"*40
    print a.isSymmetric(b1)
