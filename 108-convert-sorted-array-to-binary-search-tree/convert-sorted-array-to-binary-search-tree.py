# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_BST(left,right):
            if(left>right):
                return None
            middle = left + (right - left) // 2
            node = TreeNode(val=nums[middle])
            node.left=build_BST(left,middle-1)
            node.right=build_BST(middle+1,right)
            return node
        return build_BST(0,len(nums)-1)