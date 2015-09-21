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
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        result = []
        if root == None:
            return result

        queue = []
        queue.append(root)

        while len(queue) != 0:
            level = []

            # Debug
            # print "queue is now"
            # for i in queue:
                # print i.val,
            # print
            size = len(queue)

            for i in range(size):
                head = queue.pop()
                level.append(head.val)
                if (head.left != None):
                    queue.insert(0, head.left)
                if (head.right != None):
                    queue.insert(0, head.right)

            result.append(level)

        return result


        # write your code here


if __name__ == '__main__':
    a = Solution()


    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)

    a1.left = a2
    a1.right = a3

    aa1 = TreeNode(20)
    aa2 = TreeNode(8)
    aa3 = TreeNode(4)
    aa4 = TreeNode(12)
    aa5 = TreeNode(22)

    aa1.left = aa2
    aa1.right = aa5
    aa2.left = aa3
    aa2.right = aa4

    print a.levelOrder(aa1)
    print a.levelOrder(None)
    print a.levelOrder(a1)
