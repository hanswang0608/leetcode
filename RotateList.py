# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        
        cur = head
        length = 0
        tail = None
        while cur is not None:
            length += 1
            tail = cur
            cur = cur.next

        k = k % length
        if k == 0:
            return head

        newTail = head
        for i in range(length-k-1):
            newTail = newTail.next
        
        
        newHead = newTail.next
        tail.next = head
        newTail.next = None
        
        return newHead
# 1-2-3-4-5
#k=2 
# 4,5,1,2,3

#k=4
# 2-3-4-5-1

# [2]
#k=0

# max length = 500
# 0 <= k < 2^32-1
  
# 1-2-3-4-5
# k=2
# cur = None
# length = 5
# tail = 5

# k = 2 % 5 = 2
# slow = 3
# fast = None
# newHead = 4