# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPath(node, target):
            if not node:
                return None
            if node.val == target:
                return ""
            left = findPath(node.left, target)
            if left is not None:
                return "L" + left
            right = findPath(node.right, target)
            if right is not None:
                return "R" + right
            return None

        def findLCA(node, p, q):
            if not node or node.val == p or node.val == q:
                return node
            left = findLCA(node.left, p, q)
            right = findLCA(node.right, p, q)
            if left and right:
                return node
            return left if left else right

        lca=findLCA(root, startValue, destValue)
        pathToStart = findPath(lca, startValue)
        pathToDest = findPath(lca, destValue)
        pathUp = 'U' * len(pathToStart)
        return pathUp+pathToDest