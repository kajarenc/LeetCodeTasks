# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = float("-inf")
        is_valid = True

        def traverse(root: TreeNode):
            if not root:
                return

            nonlocal prev
            nonlocal is_valid

            traverse(root.left)

            if root.val <= prev:
                is_valid = False
            prev = root.val

            traverse(root.right)

        traverse(root)

        return is_valid