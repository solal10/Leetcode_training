# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_values(root: TreeNode) -> list:
            leaves = []
    
            def dfs(node):
                if node is None:
                    return
                if node.left is None and node.right is None:
                    leaves.append(node.val)
                dfs(node.left)
                dfs(node.right)
            dfs(root) 
            return leaves
        return get_leaf_values(root1)==get_leaf_values(root2)