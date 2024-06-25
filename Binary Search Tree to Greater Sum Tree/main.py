# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        return root

    def dfs(self, root, greater):
        if root is None:
            return 0
        right = self.dfs(root.right, greater)
        rootVal = root.val
        root.val += right + greater
        return self.dfs(root.left, root.val) + rootVal + right