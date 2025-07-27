# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        compare = set()
        temp = headA
        while(temp):
            compare.add(temp)
            temp = temp.next
        cur = headB
        while(cur):
            if(cur in compare):
                return cur
            cur = cur.next
        return None