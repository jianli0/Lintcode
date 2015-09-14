"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

import copy

class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root == None or root == A or root == B:
            return root

        # divide
        # debug
        print "jump in to left"
        if root.left == None:
            print " None %d %d " %(A.val, B.val)
        else:
            print "%d %d %d" %(root.left.val, A.val, B.val)
        left = self.lowestCommonAncestor(root.left, A, B)

        print "jump in to right"
        if root.right == None:
            print " None %d %d " %(A.val, B.val)
        else:
            print "%d %d %d" %(root.right.val, A.val, B.val)
        right = self.lowestCommonAncestor(root.right, A, B)

        # conquer
        if left != None and right != None:
            return root
        if left != None:
            return left
        if right != None:
            return right

        return None

if __name__ == '__main__':
    a = Solution()

    aa1 = TreeNode(1)
    aa2 = TreeNode(2)
    aa3 = TreeNode(3)
    aa4 = TreeNode(4)
    aa5 = TreeNode(5)
    aa6 = TreeNode(6)
    aa7 = TreeNode(7)

    aa1.left = aa2
    aa1.right = aa3
    aa2.left = aa4
    aa2.right = aa5
    aa3.left = aa6
    aa3.right = aa7

    print a.lowestCommonAncestor(aa1, aa2, aa6).val
    print a.lowestCommonAncestor(None, None, None)
    print a.lowestCommonAncestor(aa1, aa4, aa5).val
