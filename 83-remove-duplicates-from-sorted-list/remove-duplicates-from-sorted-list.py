# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        head1=head
        while head.next != None:
            if head.val == head.next.val:
                if head.next.next !=None:
                    head.next=head.next.next
                else:
                    head.next=None
            else:
                head=head.next
        return head1