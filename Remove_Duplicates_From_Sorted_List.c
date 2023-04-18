/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head)
{
    struct ListNode* temp;
    temp=head;
    if (head== NULL || head->next== NULL)
    {
        return head;
    }
    else{
    while(temp->next!=NULL)
    {
        if(temp->val==(temp->next)->val)
        {
            temp->next=temp->next->next;
        }
        else
        temp = temp->next;
    }
    return head;}


}