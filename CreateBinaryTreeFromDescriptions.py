# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        isChild = set()
        for desc in descriptions:
            isChild.add(desc[1])
            node = nodes.get(desc[0], TreeNode(desc[0]))
            child = nodes.get(desc[1], TreeNode(desc[1]))
            if desc[2]:
                node.left = child
            else:
                node.right = child
            nodes[desc[0]] = node
            nodes[desc[1]] = child
        
        for desc in descriptions:
            if desc[0] not in isChild:
                return nodes[desc[0]]