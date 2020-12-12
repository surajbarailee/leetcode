# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1, l2 = headA, headB
        len1, len2 = 0, 0
        
        while l1 is not None:
            len1 += 1
            l1 = l1.next
            
        while l2 is not None:
            len2 += 1
            l2 = l2.next
            
        diff = abs(len1 - len2)
        
        l1, l2 = headA, headB
        
        if len1 > len2:
            for _ in range(diff):
                l1 = l1.next
        elif len2 > len1:
            for _ in range(diff):
                l2 = l2.next
                
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next
            
        return l1