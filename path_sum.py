# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        def recursive_function(root, target_sum, current_sum):
            if root.left is None and root.right is None:
                if current_sum + root.val == target_sum:
                    return True
                else:
                    return False

            if root.left is None:
                return recursive_function(root.right, target_sum, current_sum + root.val)

            if root.right is None:
                return recursive_function(root.left, target_sum, current_sum + root.val)

            left_subtree_result = recursive_function(root.left, target_sum, current_sum + root.val)
            right_subtree_result = recursive_function(root.right, target_sum, current_sum + root.val)

            return left_subtree_result or right_subtree_result

        if root is None:
            return False

        return recursive_function(root, targetSum, 0)
