# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        maxSum, maxLevel = float('-inf'), 0
        curLevel = 1
        while queue:
            levelSum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                levelSum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = curLevel
            curLevel += 1
        return maxLevel