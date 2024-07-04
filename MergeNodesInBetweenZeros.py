# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        outputTail = dummy
        cur = head.next
        sum = 0
        while cur is not None:
            if cur.val != 0:
                sum += cur.val
            else:
                outputTail.next = ListNode(sum)
                outputTail = outputTail.next
                sum = 0
            cur = cur.next
        return dummy.next