"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None

class Solution:
    """
    @param root, the root of binary tree.
    @return True if it is a complete binary tree, or False.
    """
    def isComplete(self, root):
        result = self.helper(root)
        return result[2]

    def helper(self, root):
        if root == None:
            return [0,True,True]
        left = self.helper(root.left)
        right = self.helper(root.right)
        if not left[2]:
            return[-1,False,False]
        if left[0] == right[0]:
            if (not left[1] or not right[2]):
                return [-1,False,False]
            return [left[0] + 1, right[1], True]
        if left[0] == right[0] + 1:
            if(not left[2] or not right[1]):
                return [-1,False,False]
            return [left[0] + 1, False, True]
        return [-1,False,False]


