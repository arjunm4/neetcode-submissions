# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        half2 = slow.next
        
        prev = slow.next = None
        while half2:
            temp = half2.next
            half2.next = prev
            prev, half2 = half2, temp
        
        tail = head

        while prev:
            temp = tail.next
            tail.next = prev
            prev = prev.next
            tail.next.next = temp
            tail = tail.next.next
        

