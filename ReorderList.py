# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        prev = None
        cur = slow.next
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # merge two lists
        slow.next = None
        h1 = head
        h2 = prev
        while h1 and h2:
            h1_next = h1.next
            h2_next = h2.next
            h1.next = h2
            h1 = h1_next
            h2.next = h1
            h2 = h2_next
    
        
# [2,4,6,8,10]

# [2,4,6]
# [10,8]