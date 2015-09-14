"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """
    def searchRange(self, root, k1, k2):
        self.results = []
        self.searchRangeHelper(root, k1, k2)
        return self.results
        # return self.searchRangeHelper(root, k1, k2).sort()


    def searchRangeHelper(self, root, k1, k2):

        # Debug
        print "result is now %r" %self.results

        if root == None:
            return

        if root.val > k1:
            self.searchRangeHelper(root.left, k1, k2)
        if root.val >= k1 and root.val <= k2:
            self.results.append(root.val)
        if root.val < k2:
            self.searchRangeHelper(root.right, k1, k2)

if __name__ == '__main__':
    a = Solution()

    aa1 = TreeNode(20)
    aa2 = TreeNode(8)
    aa3 = TreeNode(4)
    aa4 = TreeNode(12)
    aa5 = TreeNode(22)

    aa1.left = aa2
    aa1.right = aa5
    aa2.left = aa3
    aa2.right = aa4

    print a.searchRange(aa1, 10, 22)
    print a.searchRange(None, None, None)
    print a.searchRange(aa1, 1, 3)
    print a.searchRange(aa1, 21, 22)
