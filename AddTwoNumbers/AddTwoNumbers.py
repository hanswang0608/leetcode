# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        head = l3
        carry = 0
        while l1 is not None or l2 is not None:
            first = 0
            second = 0
            if l1 is not None:
                first = l1.val
                l1 = l1.next
            if l2 is not None:
                second = l2.val
                l2 = l2.next
            temp = first + second + carry
            carry = 1 if temp >= 10 else 0
            l3.next = ListNode(temp % 10)
            l3 = l3.next
        if carry == 1:
            l3.next = ListNode(1)
        return head.next
            

    def addTwoNumbersOld(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = 0
        digit = 0
        while l1 is not None or l2 is not None:
            first = 0
            second = 0
            if l1 is not None:
                first = l1.val
                l1 = l1.next
            if l2 is not None:
                second = l2.val
                l2 = l2.next
            result += (first + second) * 10**digit
            digit += 1
        return result