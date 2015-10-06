# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        if not root:
            return None

        if p.right != None:
            return self.findLeftMost(p.right)

        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            elif p.val > root.val:
                root = root.right
            else:
                break
        return succ

    def findLeftMost(self, p):
        if p.left == None:
            return p
        else:
            return self.findLeftMost(p.left)



if __name__ == '__main__':
    a1 = TreeNode(2)
    a2 = TreeNode(1)
    a3 = TreeNode(3)

    a1.left = a2
    a1.right = a3

    a = Solution()

    if not a.inorderSuccessor({}, None) is None:
        print a.inorderSuccessor({}, None).val
    else:
        print None











