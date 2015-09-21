"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def isBalanced(self, root):
        return self.maxDepth(root) != -1

    def maxDepth(self,root):
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if (left == -1 or right == -1 or abs(left - right) > 1):
            return -1

        return max(left, right) + 1



if __name__ == '__main__':

    a = Solution()


    a1 = TreeNode(3)
    a2 = TreeNode(9)
    a3 = TreeNode(20)
    a4 = TreeNode(15)
    a5 = TreeNode(7)

    a1.left = a2
    a1.right = a3
    a3.left = a4
    a3.right = a5

    aa1 = TreeNode(3)
    aa2 = TreeNode(20)
    aa3 = TreeNode(15)
    aa4 = TreeNode(7)

    aa1.right = aa2
    aa2.left = aa3
    aa2.right = aa4

    print a.isBalanced(aa1)
    print a.isBalanced(None)
    print a.isBalanced(a1)
