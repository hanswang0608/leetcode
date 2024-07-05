# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        prev = None
        firstCrit = None
        prevCrit = None
        count = 0
        minDist = -1
        maxDist = -1
        while cur.next is not None:
            if prev is not None:
                if prev.val < cur.val > cur.next.val or prev.val > cur.val < cur.next.val:
                    if firstCrit is None:
                        firstCrit = count
                    else:
                        maxDist = count - firstCrit
                    if prevCrit is not None:
                        if minDist != -1:
                            minDist = min(minDist, count - prevCrit)
                        else:
                            minDist = count - prevCrit
                    prevCrit = count
            prev = cur
            cur = cur.next
            count += 1
        return [minDist, maxDist]