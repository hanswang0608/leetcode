# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur != None:
            nodes.append(cur)
            cur = cur.next
        
        newhead = None
        maxVal = float('-inf')
        for node in reversed(nodes):
            if node.val >= maxVal:
                maxVal = node.val
                node.next = newhead
                newhead = node
        
        return newhead