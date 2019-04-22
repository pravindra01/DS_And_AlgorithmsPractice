# Given a binary tree, return the tilt of the whole tree.

# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all 
# right subtree node values. Null node has tilt 0.

# The tilt of the whole tree is defined as the sum of all nodes' tilt.

# Example:
# Input: 
#          1
#        /   \
#       2     3
# Output: 1
# Explanation: 
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.tilt = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftSum = self._findSumAndTilt(root.left)
        rightSum = self._findSumAndTilt(root.right)

        return self.tilt + abs(leftSum - rightSum)

    def _findSumAndTilt(self, root):
        if not root:
            return 0
        # using recursion
        leftSum = self._findSumAndTilt(root.left)
        rightSum = self._findSumAndTilt(root.right)

        self.tilt += abs(leftSum - rightSum)
        return leftSum + rightSum + root.val


if __name__ == "__main__":
    test2 = TreeNode(1)
    test2.left = TreeNode(2)
    test2.right = TreeNode(3)
    test = Solution()
    print test.findTilt(test2)