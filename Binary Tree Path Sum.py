"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        res = []
        if not root:
            return None
        stack = [[root.val],[]]
        if not root.right:
            stack[1].append(root.right)
        if not root.left:
            stack[1].append(root.left)

        while len(stack[1]) != 0:
            if curt!
