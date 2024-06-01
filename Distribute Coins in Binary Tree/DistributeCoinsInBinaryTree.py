# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[0]

    def helper(self, root):
        if root is None:
            return (0,0)
        l = self.helper(root.left)
        r = self.helper(root.right)
        # amount of surplus/deficit at current node
        coin_balance = root.val - 1 + l[1] + r[1]
        # total moves to distribute is the absolute sum of balance at every node
        sum_moves = abs(coin_balance) + l[0] + r[0]
        return (sum_moves, coin_balance)