# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf(nd, leafs):
            if not nd.left and not nd.right:
                return leafs.append(nd.val)
            if nd.left: leaf(nd.left, leafs)
            if nd.right: leaf(nd.right, leafs)
        lf1, lf2 = [], []
        leaf(root1, lf1), leaf(root2, lf2)
        return lf1 == lf2