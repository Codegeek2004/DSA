/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head)
{
        struct ListNode *prev, *curr, *t;
        if (head == NULL)
            printf("List is empty");
        else
        {
            curr = head;
            prev = NULL;
            while (curr != NULL)
            {
                t = curr->next;
                curr->next = prev;
                prev = curr;
                curr = t;
            }
            head = prev;
        }
    return prev;
}