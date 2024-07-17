# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        toDelete = set(to_delete)
        roots = set([root])
        def dfs(node):
            if node is None:
                return
            if node.val in toDelete:
                if node.left is not None:
                    roots.add(node.left)
                if node.right is not None:
                    roots.add(node.right)
                if node in roots:
                    roots.remove(node)
            dfs(node.left)
            dfs(node.right)
            if node.left is not None and node.left.val in toDelete:
                node.left = None
            if node.right is not None and node.right.val in toDelete:
                node.right = None
        
        dfs(root)

        return roots