// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn add_two_numbers(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut l1 = &l1;
        let mut l2 = &l2;
        let mut head = Some(Box::new(ListNode::new(0)));
        let mut l3 = head.as_mut();
        let mut carry = 0;
        while l1.is_some() || l2.is_some() {
            let mut first = 0;
            let mut second = 0;
            if let Some(node) = l1 {
                first = node.val;
                l1 = &node.next;
            }
            if let Some(node) = l2 {
                second = node.val;
                l2 = &node.next;
            }
            let temp = first + second + carry;
            carry = if temp >= 10 { 1 } else { 0 };
            l3.as_mut().unwrap().next = Some(Box::new(ListNode::new(temp % 10)));
            l3 = l3.unwrap().next.as_mut();
        }
        if carry == 1 {
            l3.unwrap().next = Some(Box::new(ListNode::new(1)));
        }
        return head.unwrap().next;
    }
}
