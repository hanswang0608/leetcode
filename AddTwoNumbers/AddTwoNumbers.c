#define NULL 0

// Definition for singly-linked list.
struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    struct ListNode *dummy = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *l3 = dummy;
    l3->val = 0;
    l3->next = NULL;
    int carry = 0;

    while (l1 != NULL || l2 != NULL)
    {
        int sum = carry;
        if (l1 != NULL)
        {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL)
        {
            sum += l2->val;
            l2 = l2->next;
        }
        l3->next = (struct ListNode *)malloc(sizeof(struct ListNode));
        l3 = l3->next;
        l3->val = sum % 10;
        l3->next = NULL;
        carry = sum / 10;
    }

    if (carry == 1)
    {
        l3->next = (struct ListNode *)malloc(sizeof(struct ListNode));
        l3->next->val = 1;
        l3->next->next = NULL;
    }

    return dummy->next;
}