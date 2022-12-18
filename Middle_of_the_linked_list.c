/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head)
{
    struct ListNode *temp1,*temp2;
    temp1=head;
    temp2=head;
    while(temp2 != NULL && temp2->next!=NULL )
    {
        temp1 = temp1->next;
        temp2 = temp2->next->next;

    }
    return temp1;
    

}