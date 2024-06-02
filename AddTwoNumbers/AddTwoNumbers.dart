// Definition for singly-linked list.
class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

class Solution {
  ListNode? addTwoNumbers(ListNode? l1, ListNode? l2) {
    ListNode dummy = new ListNode(0);
    ListNode? l3 = dummy;
    int carry = 0;

    while (l1 != null || l2 != null) {
      int val = ((l1?.val ?? 0) + (l2?.val ?? 0) + carry);
      l3?.next = new ListNode(val % 10);
      if (l1 != null) {
        l1 = l1.next;
      }
      if (l2 != null) {
        l2 = l2.next;
      }
      carry = (val / 10).toInt();
      l3 = l3?.next;
    }

    if (carry == 1) {
      l3?.next = new ListNode(1);
    }

    return dummy.next;
  }
}
