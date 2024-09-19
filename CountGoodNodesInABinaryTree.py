# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root, maxSoFar):
            if not root:
                return
            nonlocal ans
            if root.val >= maxSoFar:
                ans += 1
            maxSoFar = max(maxSoFar, root.val)
            dfs(root.left, maxSoFar)
            dfs(root.right, maxSoFar)
        dfs(root, root.val)
        return ans