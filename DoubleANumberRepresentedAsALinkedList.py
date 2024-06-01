# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            cur = head
            next = None
            while cur != None:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev
        
        head = reverse(head)
        cur = head
        prev = None
        carry = 0
        while (cur != None):
            val = cur.val * 2
            cur.val = (val + carry) % 10
            if val > 9:
                carry = 1
            else:
                carry = 0
            prev = cur
            cur = cur.next
        if carry > 0:
            prev.next = ListNode(1, None)
        
        return reverse(head)