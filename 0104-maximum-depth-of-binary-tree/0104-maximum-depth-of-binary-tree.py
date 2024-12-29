# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def f(nd, dep):
            if nd:
                print(nd.val, dep)
                return max((dep, f(nd.left, dep + 1), f(nd.right, dep + 1)))
            return 0
        return f(root, 1)
        