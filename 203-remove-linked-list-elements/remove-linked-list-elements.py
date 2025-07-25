# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next=head
        prev,cur = temp,head
        while cur:
            if(cur.val == val):
                prev.next=cur.next
            else:
                prev=cur
            cur = cur.next
        return temp.next