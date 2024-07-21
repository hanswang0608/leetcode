# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = [0]

        # combine the left and right distance arrays and +1 depth
        def update(l, r):
            output = None
            if l is not None and r is not None:
                output = [0 for _ in range(len(l))]
                for i in reversed(range(1, 10)):
                    output[i] = l[i-1] + r[i-1]
            elif l is not None:
                output = l
                for i in reversed(range(1, 10)):
                    output[i] = l[i-1]
            else:
                output = r
                for i in reversed(range(1, 10)):
                    output[i] = r[i-1]
            return output
        
        # count pairs within distance given distance arrays
        def countPairs(l, r):
            if l is not None and r is not None:
                for i in range(distance):
                    for j in range(distance-i+1):
                        if l[i] > 0 and r[j] > 0:
                            count[0] += l[i]*r[j]
                            
        def dfs(node):
            if node is None:
                return None
            if node.left is None and node.right is None:
                return [0,1,0,0,0,0,0,0,0,0]
            left = dfs(node.left)
            right = dfs(node.right)
            countPairs(left, right)
            return update(left, right)

        dfs(root)

        return count[0]
